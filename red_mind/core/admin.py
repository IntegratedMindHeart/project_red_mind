from django.contrib import admin
from .models import MovieRecord

# Register your models here.

@admin.register(MovieRecord)
class MovieRecordAdmin(admin.ModelAdmin):
    list_display=('id','movie_name','date_time')