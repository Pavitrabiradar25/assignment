from django.db import models
from django.contrib.auth.models import User

class TrackTable(models.Model):
	artist = models.ForeignKey(User,on_delete=models.CASCADE)
	album = models.CharField(max_length=50)
	mediatrackid = models.IntegerField()
	invoice = models.CharField(max_length=50)
	customer = models.CharField(max_length=50)