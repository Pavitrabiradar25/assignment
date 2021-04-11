from django.contrib import admin
from .models import TrackTable
# Register your models here.

@admin.register(TrackTable)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['id', 'artist', 'album', 'mediatrackid','invoice','customer']