import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.BooleanField()
    isSuperUSer=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name

class Order(models.Model):
    user=models.ForeignKey(User)
    event = models.ForeignKey('Event')
    cost=models.IntegerField()
    number=models.IntegerField()
    rahgiriCode=models.IntegerField()
    ticket_type = models.ForeignKey('EventTicketType')
    date = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    event = models.ForeignKey('Event')
    type=models.CharField(max_length=32)
    price=models.IntegerField()
    seat=models.IntegerField()

class Event(models.Model):
    #user=models.ForeignKey('UserProfile')
    date=models.DateField()
    # ticketsLeft=models.IntegerField()
    # ticketsSold=models.IntegerField(default=0)
    category = models.ForeignKey('Category')
    subCategory = models.ForeignKey('SubCategory')
    description= models.TextField()
    subject=models.CharField(max_length=32)
    finishDate=models.DateField()
    #price=models.IntegerField()
    photo = models.FileField(upload_to='event_photoes/')
    #scoredUsers = models.ForeignKey('Scorers', null=True)
    score=models.FloatField(default=0)
    numberofScorers=models.IntegerField(default=0)

    def ticketsLeft(self):
        return self.eventtickettype_set.all().aggregate(x=Sum('tickets'))['x'] or 0


class EventTicketType(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey('Event')
    price = models.IntegerField()
    tickets = models.IntegerField()


class Scorers(models.Model):
    scorers= models.ManyToManyField('UserProfile')

class Comment(models.Model):
    author=models.ForeignKey('UserProfile')
    event=models.ForeignKey('Event')
    content=models.TextField()
    time=models.DateTimeField(default=datetime.datetime.now)
    numberOfLikes=models.IntegerField(default=0)
    #likes=models.ForeignKey('Likers')
    def __str__(self):
        return self.content
class Category(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=32)
    daste=models.ForeignKey('Category')

    def __str__(self):
        return self.name


class Likers(models.Model):
    user=models.ManyToManyField('UserProfile')