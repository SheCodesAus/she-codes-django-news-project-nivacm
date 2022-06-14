from django.db import models
from django.contrib.auth import get_user_model
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author =models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    url = models.URLField(max_length = 200, default="")
    category = models.ForeignKey('news.Category', related_name='stories', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    story_img = models.CharField(max_length=500, default="https://i.picsum.photos/id/1060/5598/3732.jpg?hmac=31kU0jp5ejnPTdEt-8tAXU5sE-buU-y1W1qk_BsiUC8")

    class Meta:
        ordering = ['-pub_date']


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name




class Comment(models.Model):
    newsstory = models.ForeignKey(NewsStory, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return '%s - %s' % (self.newsstory.title, self.name)


# pensar en el autor.