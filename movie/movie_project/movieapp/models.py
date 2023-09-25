from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=255)
    year=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='movie_image')

    def __str__(self):
        return self.name
