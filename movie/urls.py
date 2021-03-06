"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movie_server.views import MovieListView, AddMovieView, DeleteView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', MovieListView.as_view(), name='list-movies'),
    url(r'^add_movie/', AddMovieView.as_view(), name='add-movies'),
    url(r'^del_movie/', DelMovieView.as_view(), name='add-movies'),
    
    
    
]
