from django import forms

from . models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','movie_desc','movie_year','movie_image']