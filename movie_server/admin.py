from django.contrib import admin
from movie_server.models import Person, Movie, Role
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display =('title',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    list_display =('first_name','last_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
    #list_display =('role',)
