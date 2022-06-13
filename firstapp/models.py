#from typing_extensions import Required
from asyncio.windows_events import NULL
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Cluster(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=1,
                validators=[MaxValueValidator(1),MinValueValidator(1)])
    duration= models.IntegerField(default=0)
    availability = models.DateField()
    available = models.BooleanField(default = NULL)
    #datum überprüfen

class freeDates(models.Model):
    date = models.DateField()   

# not used yet, using the defaul "User" model from django
class Nutzer(models.Model):
    matrikelnummer = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    def str(self):
        return '%s'%self.username


class Todo(models.Model):
    title = models.CharField(max_length=250)
    deadline = models.DateField()
    percent = models.PositiveIntegerField(default=0,
                validators=[MaxValueValidator(100),MinValueValidator(0)])

class Reservation(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, default = NULL)
    clus_name = models.CharField(max_length=100)
    #user_booking = models.ForeignKey(Nutzer, on_delete=models.CASCADE, default = NULL)
    user_name = models.CharField(max_length=250 , default='')
    duration= models.PositiveIntegerField()
    quantity = models.IntegerField(default = 1)
    #status = models.BooleanField(default = NULL)




#python manage.py makemigrations --> python manage.py migrate
