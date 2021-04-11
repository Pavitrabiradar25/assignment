from .models import TrackTable
from .serializers import TrackTableSerializer
from rest_framework import viewsets

class TrackTableModelViewSet(viewsets.ModelViewSet):
  queryset = TrackTable.objects.all()
  serializer_class = TrackTableSerializer