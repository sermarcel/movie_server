from django.shortcuts import render
from django.shortcuts import render, redirect
from movie_server.models import Movie


# Create your views here.
def movies_list(request):
    cont={}
    cont['movies']=Movie.objects.order_by('-year').all()
    
    print(cont)
    return render(request, 'list_movies.html', cont)