from django.db import models
import uuid

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    tags = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.title
    


