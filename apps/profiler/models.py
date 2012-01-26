# profiler.models
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import settings
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
from ts.models import Ad



class Mess(models.Model):
	sender = models.ForeignKey(User,related_name='messsend',blank=True,null=True)
	receiver = models.ForeignKey(User,related_name='messrec')
	email = models.EmailField(blank=True)
	name = models.CharField(blank=True, max_length=100)
	subject = models.CharField(max_length=200,blank=False)
	message = models.TextField(blank=False)
	written = models.DateTimeField(auto_now_add=True)
	unread = models.BooleanField(default=True)
	replied = models.ForeignKey('self',blank=True,null=True)

	def __unicode__(self):
		return self.subject 
	
	class Meta:
		ordering = ('-written',)

	def save(self):
		super(Mess, self).save()
		s = self
		subject = 'TimeshareRentals.com message: ' + self.subject
		if self.sender:
			content = '''%s,

			%s sent you a message on TimeshareRentals.com with the subject "%s".

			Message: %s


			You can respond <a href='http://timesharerentals.com/profile/messages/%s/%s/'>here</a>.

			Thank you,
			TimeshareRentals.com
			''' %(self.receiver.username,self.receiver.username,self.subject,self.message,self.receiver.id,self.id)
		else:
			content = '''%s,

			%s, with the email: %s sent you a message on TimeshareRentals.com with the subject "%s".

			Message: %s


			You can respond <a href='http://timesharerentals.com/profile/messages/%s/%s/'>here</a>.

			Thank you,
			TimeshareRentals.com
			''' %(self.receiver.username,self.name,self.email,self.subject,self.message,self.receiver.id,self.id)
		fromemail = settings.CONTACT_EMAIL
		toemail = [self.receiver.email,]
		send_mail(subject,content,fromemail,toemail)



class EmailReset(models.Model):
	email = models.EmailField(blank=True, max_length=100)
	expires = models.DateTimeField()
	key = models.CharField(blank=True, max_length=100)
	
	def __unicode__(self):
		return self.email