from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    