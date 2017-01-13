from django.db import models

# Create your models here.

RANKING =( 
        (1,'1'), 
        (2,'2'),
         (3,'3'), 
         (4,'4'), 
         (5,'5')
         )




class Person(models.Model):

    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Movie(models.Model):

    title=models.CharField(max_length=128)
    director=models.ForeignKey(Person, related_name='dirs')
    screenplay=models.ForeignKey(Person, related_name='scres')
    year = models.IntegerField(null=True)
    ranking=models.IntegerField(choices=RANKING, default=-1)
    starring=models.ManyToManyField(Person, through='Role')

    def __str__(self):
        return self.title

class Role(models.Model):
    
    movie=models.ForeignKey(Movie)
    actor=models.ForeignKey(Person)

    

