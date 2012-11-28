from django.conf import settings
from django.core.management.base import BaseCommand, NoArgsCommand
from datetime import datetime, timedelta
from ts.models import Ad
import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail


class Command(BaseCommand):
	args = ''
	help = 'Check all the ads and notify the owner if they are expiring.'
	
	def handle(self, *args, **options):
		def send_notif(ad,when):
			subject = 'Your ad on TimeshareRentals.com is expiring %s.'  % when
			content = '''%s,
					Your ad "%s", on TimeshareRentals.com is expiring %s.
					You can renew it by replying to this email and letting
					us know. If you do not wish to renew it, 
					simply let it expire. Thanks for placing your ad with us.

					Timesharerentals.com
			''' %(ad.creator,ad,when,ad.creator.id)
			fromemail = settings.CONTACT_EMAIL
			toemail = [ad.creator.email,]
			send_mail(subject,content,fromemail,toemail)
		today = datetime.today().date()
		twfn = today + timedelta(weeks=2)
		ads = Ad.objects.exclude(adtype=4)
		notifs = 0
		for ad in ads:
			# print 'twfn: %s  and aed: %s' %(twfn,ad.expiration_date)
			if twfn == ad.expiration_date:
				notifs += 1
				print '%s is expiring in two weeks\n' % ad.name
				send_notif(ad,'in 2 weeks')
			if today == ad.expiration_date:
				notifs += 1
				print '%s is expiring today\n' % ad.name
				send_notif(ad,'today')
		print 'Notify ran and sent %s email(s).\n' % str(notifs)
		# logging.info('There are %s non-Gold Ads.\n' % str(len(ads)))
