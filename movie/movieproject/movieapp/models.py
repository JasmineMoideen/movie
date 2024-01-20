from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.TextField()
    movie_desc = models.TextField()
    movie_year = models.IntegerField()
    movie_image = models.ImageField(upload_to='pics')