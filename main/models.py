from django.db import models



class item(models.Model):
    url = models.CharField(max_length=100)
    youtube_vid = models.CharField(max_length=100, blank=True)
    pic_url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
