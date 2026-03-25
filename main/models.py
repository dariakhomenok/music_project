from django.db import models

class Genre(models.Model):
    name_eng = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_ru

class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    executor = models.CharField(max_length=500, null=True)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title