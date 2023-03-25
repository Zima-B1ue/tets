from django.db import models


# Create your models here.

class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(0.0)
    created_date = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
