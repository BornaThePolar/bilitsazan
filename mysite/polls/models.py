import datetime
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.BooleanField()
    isSuperUSer=models.BooleanField(default=False)


class Order(models.Model):
    user=models.ForeignKey('UserProfile')
    event = models.ForeignKey('Event')
    cost=models.IntegerField()
    number=models.IntegerField()

class Buy(models.Model):
    rahgiriCode=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField()

class Ticket(models.Model):
    event = models.ForeignKey('Event')
    type=models.CharField(max_length=32)
    price=models.IntegerField()
    seat=models.IntegerField()

class Event(models.Model):
    user=models.ForeignKey('UserProfile')
    date=models.DateField()
    ticketsLeft=models.IntegerField()
    ticketsSold=models.IntegerField()
    category = models.ForeignKey('Category')
    subCategory = models.ForeignKey('SubCategory')
    description= models.TextField()
    subject=models.CharField(max_length=32)
    finishDate=models.DateField()
    price=models.IntegerField()
    photo = models.FileField(upload_to='static/Photos/Users/')
    scoredUsers = models.ForeignKey('Scorers')
    score=models.FloatField()

class Scorers(models.Model):
    scorers= models.ManyToManyField('UserProfile')

class Comment(models.Model):
    author=models.ForeignKey('UserProfile')
    content=models.TextField()
    time=models.DateTimeField(default=datetime.datetime.now)
    numberOfLikes=models.IntegerField()
    likes=models.ForeignKey('Likers')

class Category(models.Model):
    name=models.CharField(max_length=32)

class SubCategory(models.Model):
    name=models.CharField(max_length=32)
    daste=models.ForeignKey('Category')

class Likers(models.Model):
    user=models.ManyToManyField('UserProfile')