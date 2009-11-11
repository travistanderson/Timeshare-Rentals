# ts/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from photologue.models import Photo, Gallery


class Country(models.Model):
	name = models.CharField(blank=True,  max_length=128)
	iso = models.CharField(max_length=2,)
	iso3 = models.CharField(max_length=3, null=True)
	flag = models.URLField(blank=True,)
	
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		ordering = ('name',)
		
	def __unicode__(self):
		return self.name

class Comment(models.Model):
	comment = models.TextField(blank=True)
	user = models.ForeignKey(User)
	premod = models.BooleanField(default=False)
	date_created = models.DateField(blank=True,auto_now_add=True)

class ResortType(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

	
class Resort(models.Model):
	name = models.ForeignKey(ResortType)
	branch = models.CharField(max_length=200)
	description = models.TextField()	
	picture = models.ForeignKey(Photo, blank=True, null=True)
	email = models.EmailField()
	url = models.URLField()
	address = models.CharField(max_length=200)
	address_country = models.ForeignKey(Country)
	premod = models.BooleanField(default=False)
	comment = models.ForeignKey(Comment, blank=True)
	
	def __unicode__(self):
		return self.name

class Ad(models.Model):
	DURATION_CHOICES = ((1,'6 Month'),(2,'12 Months'),(3,'Lifetime'),)
	name = models.CharField(max_length=100)
	description = models.TextField()
	gallery = models.ForeignKey(Gallery, blank=True, null=True)
	resort = models.ForeignKey(Resort, blank=True)
	creator = models.ForeignKey(User)
	start_ad = models.DateField(blank=True,auto_now_add=True)
	start_room = models.DateField(blank=True)
	end_room = models.DateField(blank=True)
	premium = models.BooleanField(default=False)
	premod = models.BooleanField(default=False)
	duration = models.IntegerField(choices=DURATION_CHOICES,blank=True,default=1)
	
	def __unicode__(self):
		return self.name


class Email(models.Model):
	EVENT_CHOICES = ((1,'Ad is Created'),(2,'TS is available'),(3,'TS is done being available'),(4,'Ad expires'),)
	name = models.CharField(max_length=100)
	content = models.TextField()
	days = models.IntegerField(blank=True, null=True)
	before = models.BooleanField(default=True)
	event = models.IntegerField(choices=EVENT_CHOICES,blank=True, null=True)
	
	def __unicode__(self):
		return self.name