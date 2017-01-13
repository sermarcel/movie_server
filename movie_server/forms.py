from django import forms
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple
from movie_server.views import movies_list


'''
class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['title','year','director']
   '''     