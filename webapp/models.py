from django.db import models

# Create your models here.
#"""this is  a model for the our data of album and song """
class Album(models.Model):
    title = models.CharField(max_length=100) #title of song
    genre=models.CharField(max_length=40) #type of music like pop etc
    artist=models.CharField(max_length=100) #artist name of album
    album_logo=models.CharField(max_length=1000) #album logo

    def __str__(self):
        return "album:"+self.title+"\nartist:"+self.artist

class Song(models.Model):
    alb_id=models.ForeignKey(Album,on_delete=models.CASCADE)#on_delete delete the song on delete of albums
    stitle=models.CharField(max_length=500) #song title
    ftype=models.CharField(max_length=10) #file type like mp3 etc
    sartist=models.CharField(max_length=100) #song artist

    def __str__(self):
        return "song:\n" + self.stitle + "artist:\n" + self.sartist