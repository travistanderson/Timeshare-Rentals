# pages/models.py
from django.db import models
from django.contrib.sites.models import Site
import datetime
# from django.db.models.query import DoesNotExist 

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True,unique=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	templatr = models.CharField(max_length=70, blank=True,help_text="optional",)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return self.url

	def get_absolute_url(self):
		return self.url
		
	def save(self):
		super(Page, self).save()
		s = self
		# try:
		old = Revpage.objects.filter(page=s)
		if old.count() < 1:
			r = Revpage(page=s,content=s.content,number=1,updated=datetime.datetime.now())
			r.save()
		else:
			num = old.count() -1
			old = old[num]
			if old.content != s.content:
				t = Revpage.objects.filter(page=s).count() + 1
				r = Revpage(page=s,content=s.content,number=t,updated=datetime.datetime.now())
				r.save()


class Revpage(models.Model):
	page = models.ForeignKey(Page)
	content = models.TextField(blank=True)
	number = models.IntegerField()
	updated = models.DateField(default=datetime.datetime.now)

	class Meta:
		ordering = ('page','number')

	def __unicode__(self):
		return u"Revision %s on %s" % (self.number, self.page)
		


