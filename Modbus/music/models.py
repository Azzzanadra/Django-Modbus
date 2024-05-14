from django.db import models

# Create your models here.
#ignore
class Album(models.Model):
    artists = models.CharField(max_length = 150)
    album_title = models.CharField(max_length = 350)
    genre = models.CharField(max_length = 50)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.album_title+ ", "+ self.artists 

#ignore
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title =  models.CharField(max_length = 250)

    def __str__(self):
        return self.song_title

#fan objects
class Fan(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default = 0)
    max_speed = models.IntegerField(default = 0)
    set_speed = models.IntegerField(default = 0)
    actual_speed = models.IntegerField(default = 0)

 