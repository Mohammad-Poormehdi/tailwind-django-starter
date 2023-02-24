from django.db import models

# Create your models here.


class Post(models.Model):
    thumbnail = models.ImageField(upload_to='files/')
    title = models.CharField(max_length=200)
    intro = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    reading_time = models.PositiveBigIntegerField()
    slug = models.SlugField(unique=True,)
    def __str__(self):
        return self.title