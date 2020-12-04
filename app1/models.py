from django.db import models
from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video_title = models.CharField(max_length=300)
    video = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return(self.video_title[0:15])
   
