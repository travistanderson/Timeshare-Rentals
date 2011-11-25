# ts/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from photologue.models import Photo, Gallery
from django.utils.safestring import mark_safe
import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
ADTYPES = ((1,'Free'),(2,'Bronze'),(3,'Silver'),(4,'Gold'),)
PRICETYPES = ((1,'Night'),(2,'Month'),)


class Photoo(Photo):
	orderer = models.IntegerField(default=1,blank=True, null=True)
	
	class Meta:
		ordering = ['orderer']
		get_latest_by = "orderer"
		
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
	iso = models.CharField(max_length=20,)
	
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		ordering = ('name',)
		
	def __unicode__(self):
		return self.name
	
	def flag(self):
		return mark_safe('<img src="/site_media/images/flagsbig/' + str(self.iso) + '.png" style="width:80px;"></img>')
	flag.allow_tags=True


class Comment(models.Model):
	comment = models.TextField(blank=True)
	user = models.ForeignKey(User)
	premod = models.BooleanField(default=False)
	date_created = models.DateField(blank=True,auto_now_add=True)
	
	def __unicode__(self):
		return str(self.user) + ' - ' + str(self.id) + ' - ' + str(self.comment[0:20])


	
class Resort(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)	
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
	price = models.DecimalField(max_digits=10, decimal_places=2)
	priceunit = models.IntegerField(choices=PRICETYPES,blank=True, null=True)
		
	class Meta:
		ordering = ('-start_ad',)
		permissions = (('view_paypal','Can see the results of Paypal auth return.'),)

	def __unicode__(self):
		return self.name

	def first(self):
		for photo in self.photos.all():
			if photo.orderer == 1:
				return photo
				break

	def photolist(self):
		return self.photos.order_by('orderer')

	def save(self,*args,**kwargs):
		s = self
		new = True
		try:		# this checks to see if it is new or not
			a = Ad.objects.get(id=s.id)
			new = False
			action = 'edited'
		except Exception, e:
			a = None
			action = 'created'
		super(Ad, self).save(*args,**kwargs)
		subject = 'TSR: An ad was just %s. %s'  %(action,self.name)
		content = '''Annie,
				%s just %s the ad %s.
				Check it for moderation <a href='http://timesharerentals.com/admin/ts/ad/%s/'>here</a> when you get a chance.
				
				Timesharerentals.com
		''' %(self.creator,action,self.name,self.id)
		fromemail = settings.CONTACT_EMAIL
		toemail = ['modernarrangements@gmail.com',]
		send_mail(subject,content,fromemail,toemail)



class Email(models.Model):
	EVENT_CHOICES = ((1,'Ad is Created'),(2,'TS is available'),(3,'TS is done being available'),(4,'Ad expires'),)
	name = models.CharField(max_length=100)
	content = models.TextField()
	days = models.IntegerField(blank=True, null=True)
	event = models.IntegerField(choices=EVENT_CHOICES,blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		


