from encodings.punycode import T
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    STATUS_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        to = Category,
        on_delete=models.CASCADE,
        # default=1,
        related_name='posts',
        null=True
    )

    title = models.CharField(max_length=250, help_text="This is some the title")

    excerpt = models.TextField(null=True, blank=True)

    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True)

    publish = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        default=1
    )

    content = models.TextField(null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_OPTIONS,
        default='draft'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        # verbose_name = "Post"
        verbose_name_plural = "Posts"
        