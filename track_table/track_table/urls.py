from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('TrackTable', views.TrackTableModelViewSet, basename='TrackTable')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
