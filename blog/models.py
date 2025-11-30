from turtle import mode
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=224)
    
    def __str__(self):
        self.title
        
