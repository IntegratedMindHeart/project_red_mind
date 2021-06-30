from django.db import models

# Create your models here.

class MovieRecord(models.Model):
    id=models.AutoField(primary_key=True)
    movie_name=models.CharField(max_length=200)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name