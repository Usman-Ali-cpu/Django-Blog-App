from django.db import models

# Create your models here.


class Article(models.Model):
    """
    Articles Model
    """
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    