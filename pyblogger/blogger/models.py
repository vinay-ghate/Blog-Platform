from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title