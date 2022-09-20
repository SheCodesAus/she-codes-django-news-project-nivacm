from django.contrib import admin
from .models import Category, NewsStory, Comment

# Register your models here.
# admin.site.register(Category)
admin.site.register(NewsStory)
admin.site.register(Comment)