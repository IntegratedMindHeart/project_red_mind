from django import forms
from .models import MovieRecord

class MovieRecordForm(forms.ModelForm):
    class Meta:
        model=MovieRecord
        fields=('movie_name',)
        widgets={
            'movie_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter movie name'})
        }