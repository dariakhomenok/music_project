from django.db import models

class Genre(models.Model):
    name_eng = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_ru

class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.title
    
class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)
    
    def __str__(self):
        return self.name