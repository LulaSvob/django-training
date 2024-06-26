from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    # Django automatically adds 'id' as a primary key field.
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    

class Review(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchagain = models.BooleanField()
    
    def __str__(self):
        return self.text