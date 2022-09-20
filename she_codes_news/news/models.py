from django.db import models
from django.contrib.auth import get_user_model
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author =models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    url= models.URLField(max_length = 200, default="")
    content = models.TextField()
    
    class Meta:
        ordering = ['-pub_date']


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name




class Comment(models.Model):
    newsstory = models.ForeignKey(NewsStory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return '%s - %s' % (self.newsstory.title, self.name)


