from django.contrib.auth.models import User
from mailer import send_mail
userlist = [['hgreene','hgreene12@hotmail.com','bi5hap4v'],['roxenford','gvrjox@msn.com','eaf5of6y'],['gina','gina@shoplove007.com','cy5woj8n'],['dlane','davidvlane@hotmail.com','dic5non7'],['djunk','dajunked@hotmail.com','gryen9pa'],['mlinnell','hbchica@hotmail.com','eef3net4'],['lcercone','ljcercone@earthlink.ne','lal6ab3v'],['avrilc','avrilc81@hotmail.com','tax4hor7'],['jmannino','coachmann1@aol.com','dred6jeb'],['dgraham','reservations@mtbakerlodging.com','ey9roam6'],['esordo','myreplies@excite.com','viv9ar5a'],['gerri','lynchmanzo@gmail.com','whet9il2y'],['jfearn','jfearn@wesellu.com','hi8hif4yu'],['smccarthy','SarahMcCarthy83@yahoo.com','ic9dimt4e'],['fleverone','Fleverone@aol.com','wev5av8te'],['acasey','avrilc81@hotmail.com','coyt5lir4'],['pmartinez','PHYLLIS626@YAHOO.COM','ulf3on3je'],['adillon','adillon10@hotmail.com','vej4le5hi'],['splotkin','shelly821@verizon.net','dank7ep2v'],['tdavis','tlddavis15@aol.com','tof2par8u'],['wnicholson','Nichplas@aol.com','je9ov6yit']]
fromemail = 'timesharerentalscontact@gmail.com'
subject = 'Timesharerentals.com has redesigned.'

for user in userlist:
    toemail = [user[1],]
    u = User.objects.get(username = str(user[0]))
    content = '''
Dear %s,

Timesharerentals.com has just completed a redesign of the entire site. You are receiving this email because you have an ad listed with us. The new site allows you to edit your own ads, upload pictures of your timeshare and exchange messages directly with other users. There is an improved search function which will make it more likely for your ad to be found and for your timeshare to be rented. Also users can send you messages from the site about your ad. You can create new ads yourself. We have paid ads with premium features and a free ad as well.

Your old ad has been moved to the new site and can be seen <a href='http://timesharerentals.com/profile/%s/'>here</a>. We have created a user account for you.
Username: %s
Password: %s

You can login <a href='http://timesharerentals.com/profile/login/'>here</a>. We recommend that you login at your earliest convenience and change the password to one of your own choosing. We have '%s' on record as your contact email address. You can change it as well on your profile page <a href='http://timesharerentals.com/profile/settings/%s/'>here</a>.

Thank you for using Timesharerentals.com. We hope the new site will be a benefit to you.

Timesharerentals.com''' %(user[0],u.id,u.username,user[2],user[1],u.id)
    send_mail(subject,content,fromemail,toemail)




localuserlist = [['travis','travistanderson@gmail.com','somepaswwwword'],]

expireduserlist = [['msirinek','msirinek@yahoo.com','yey2thov'],['tlindstrom','theresa.lindstrom@kohler.com','u5grac2f'],['whampton','wadehampton@earthlink.net','tic9eawd'],['ptalerico','prock103@yahoo.com','liej2eir'],['psinger','handsonheal@comcast.net','ow9es7oi'],['jdamico','jldamico@telus.net','en4ral7a'],['tsnee','tanya_snee@hotmail.com','ai6wram7'],['smccowan','shawn.mccowan@gmail.com','kled3wat'],['gpye','gpye@loyalty.com','queyt7ay'],['mgarvey','marcusgarvey0164@yahoo.com','daw7oik5'],['rrace','rgrrace@bellsouth.net','biv4bov2y']]
for user in expireduserlist:
    toemail = [user[1],]
    u = User.objects.get(username = str(user[0]))
    content = '''
Dear %s,

Timesharerentals.com has just completed a redesign of the entire site. You are receiving this email because you had an ad listed with us that recently expired. The new site allows you to edit your own ads, upload pictures of your timeshare and exchange messages directly with other users. There is an improved search function which will make it more likely for your ad to be found and for your timeshare to be rented. Also users can send you messages from the site about your ad. You can create new ads yourself. We have paid ads with premium features and a free ad as well. If you have any need to advertise your timeshare again, please think of using us.

Because you recently had an ad, we have created a user account for you.
Username: %s
Password: %s

You can login <a href='http://timesharerentals.com/profile/login/'>here</a>. We recommend that you login at your earliest convenience and change the password to one of your own choosing. We have '%s' on record as your contact email address. You can change it as well on your profile page <a href='http://timesharerentals.com/profile/settings/%s/'>here</a>.

Thank you for using Timesharerentals.com. We hope the new site will be a benefit to you.

Timesharerentals.com''' %(user[0],u.username,user[2],user[1],u.id)
    send_mail(subject,content,fromemail,toemail)



