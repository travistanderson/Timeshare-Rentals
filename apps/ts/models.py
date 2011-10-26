# ts/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from photologue.models import Photo, Gallery
import settings


class Photoo(Photo):
	orderer = models.IntegerField(default=1,blank=True, null=True)
	
	def ad(self):
		try:
			return self.ad_set.all()[0]
		except Exception, e:
			return 'hello'
			
	def user(self):
		try:
			return self.ad_set.all()[0].creator
		except Exception, e:
			return 'hello'

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


	
class Resort(models.Model):
	name = models.CharField(max_length=200)
	branch = models.CharField(max_length=200,blank=True, null=True)
	description = models.TextField(blank=True, null=True)	
	picture = models.ForeignKey(Photo, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	address = models.CharField(max_length=200, blank=True,)
	address_country = models.ForeignKey(Country,blank=True,null=True)
	premod = models.BooleanField(default=False)
	comment = models.ManyToManyField(Comment, blank=True, null=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = 'Resort'
		verbose_name_plural = 'Resorts'
		ordering = ('name',)


class Ad(models.Model):
	ADTYPES = ((1,'Free'),(2,'Bronze'),(3,'Silver'),(4,'Gold'),)
	name = models.CharField(max_length=80)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	photos = models.ManyToManyField(Photoo, blank=True, null=True)
	resort = models.ForeignKey(Resort, blank=True, null=True)
	creator = models.ForeignKey(User)
	start_ad = models.DateField(blank=True,auto_now_add=True)
	start_room = models.DateField(blank=True)
	end_room = models.DateField(blank=True)
	adtype = models.IntegerField(choices=ADTYPES,blank=True, null=True)
	premod = models.BooleanField(default=False)
	paid = models.BooleanField(default=False)
	expiration_date = models.DateField(blank=True,)
	
	def __unicode__(self):
		return self.name

	def first(self):
		for photo in self.photos.all():
			if photo.orderer == 1:
				return photo
				break

	def photolist(self):
		return self.photos.order_by('orderer')		


class Email(models.Model):
	EVENT_CHOICES = ((1,'Ad is Created'),(2,'TS is available'),(3,'TS is done being available'),(4,'Ad expires'),)
	name = models.CharField(max_length=100)
	content = models.TextField()
	days = models.IntegerField(blank=True, null=True)
	event = models.IntegerField(choices=EVENT_CHOICES,blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		


