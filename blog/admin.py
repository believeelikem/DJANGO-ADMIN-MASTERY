from calendar import c
from pyexpat import model
from symtable import Class
import django
import django.apps
from django.contrib import admin
from .models import *



class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin area"
    # index_title = "Something here"
    site_title = "B"
    login_template = "blog/admin/login.html"
   
    
# blog_site = BlogAdminArea(name="BlogAdmin")
blog_site2 = BlogAdminArea(name="BlogAdmin")
# blog_site2.register(Post)


# admin.site.register(Post)
# admin.site.register(Category)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ["title", "author"] # the fields for adding new data

# models = django.apps.apps.get_models()    
# print(models)

# admin.site.register(Post)
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
    
# admin.site.unregister(django.contrib.sessions.models.Session)

# TEXT  = "Some text here "
# class PostAdmin(admin.ModelAdmin):
#     # fields = [("slug","title"), "author"] # the fields for adding new data, we group on one line with ()
    
#     fieldsets = (
#         ("Section 1", {
#             "fields":("title","author",),
#             "description":"%s" % TEXT,
#         }),
#         ("Section 2", {
#             "fields":("slug",),
#             "classes":("collapse",),
#         }),
#     )
    
    
# admin.site.register(Post, PostAdmin)


# from django import forms

# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
        
#         self.fields["title"].help_text = "New Help text"
        
#     class Meta:
#         model = Post
#         exclude = ("slug",)
        

# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm
    
    
# admin.site.register(Post, PostFormAdmin)
from django_summernote.admin import SummernoteModelAdmin

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area" 

blog_site = BlogAdminArea(name="BlogAdmin")
# blog_site.register(Post)
# admin.site.unregister(Post)

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    
# admin.site.register(Post, SummerAdmin)
blog_site.register(Post, SummerAdmin)
