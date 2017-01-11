from django.db import models

# Create your models here.

RANKING= (1,2,3,4,5)




class Person(models.Model):

    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    
class Movie(models.Model):

    title=models.CharField(max_length=128)
    director=models.ForeignKey(Person)
    screenplay=models.ForeignKey(Person)
    year = models.IntegerField(null=True)
    ranking=models.IntegerField(choices=RANKING, default=-1)
    starring=models.ManyToManyField(Person, through='Role')

class Role(models.Model):

    role=models.CharField(max_length=128, null=True),
    movie=models.
    actor=models.
    

