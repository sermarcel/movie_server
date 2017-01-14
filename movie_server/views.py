from django.shortcuts import render
from django.shortcuts import render, redirect
from movie_server.models import Movie, Person
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView




# Create your views here.
class MovieListView(ListView):
    model=Movie    
    fields='__all__'
    #sucess_url=''

class AddMovieView(CreateView):
    
    model=Movie
    fields=('title', 'director', 'screenplay', 'year', 'ranking')
    #exclude=('starring',)
    # sucess_url=''
    

