import datetime
from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images')
  email = models.EmailField(unique=True)
  phoneno=models.IntegerField(default=0)
  post = models.CharField(max_length=100)
  order=models.SmallIntegerField(default=0)
  year = models.IntegerField(default=0)
  linkedin = models.CharField(max_length=200)
  facebook = models.CharField(max_length=200)
  instagram = models.CharField(max_length=200)
  def __str__(self):
         return self.name

class Alumni(models.Model):
  name = models.CharField(max_length=100)
  image=models.ImageField(upload_to='images/Alumni')
  email = models.EmailField(unique=True)
  phoneno=models.IntegerField(default=0)
  passyear = models.IntegerField(default=0)
  linkedin = models.CharField(max_length=200)
  facebook = models.CharField(max_length=200)
  instagram = models.CharField(max_length=200)
  def __str__(self):
         return self.name

class Event(models.Model):
  EventName = models.CharField(max_length=100)
  Image=models.ImageField(upload_to='images/Events')
  StartDate = models.DateTimeField(default=datetime.datetime.today())
  EndDate = models.DateTimeField(default=datetime.datetime.today())
  Location = models.CharField(max_length=500,blank=True)
  Link = models.CharField(max_length=5000,blank=True,default=" ")
  Description = models.CharField(max_length=5000,blank=True)
  EventTense = models.CharField(max_length=100,blank=True)
  
  def __str__(self):
         return self.EventName


class gallery(models.Model):
  eventName = models.CharField(max_length=100)
  Image=models.ImageField(upload_to='images/gallery')
  imgDate = models.DateTimeField(default=datetime.datetime.today())
  
  def __str__(self):
        return self.eventName
  

class blog(models.Model):
  blogName = models.CharField(max_length=100)
  Image = models.ImageField(upload_to='images/blog')
  StartDate = models.DateTimeField(default=datetime.datetime.today())
  Link = models.CharField(max_length=5000, blank=True, default=" ")
  Description = models.CharField(max_length=5000, blank=True)


  def __str__(self):
    return self.blogName

class sponsers(models.Model):
  Image=models.ImageField(upload_to='images/sponsers')
  Link = models.CharField(max_length=5000,blank=True,default="no link")

class Contact(models.Model):
  name = models.CharField(max_length=100)
  phone = models.IntegerField(default=0)
  email = models.EmailField()
  message = models.CharField(max_length=5000,blank=True)
  
  def __str__(self):
    return self.name