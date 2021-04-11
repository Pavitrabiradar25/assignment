from rest_framework import serializers
from .models import TrackTable

class TrackTableSerializer(serializers.ModelSerializer):
 class Meta:
  model = TrackTable
  fields =  ['id', 'artist', 'album', 'mediatrackid','invoice','customer']