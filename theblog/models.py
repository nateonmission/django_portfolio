from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)
    slug = models.CharField(max_length=75)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.author} written on {self.date_created}"