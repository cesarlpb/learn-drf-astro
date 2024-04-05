from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

