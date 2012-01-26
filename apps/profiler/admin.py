# profiler/admin.py
from django.contrib import admin
from profiler.models import Mess, EmailReset



class MessAdmin(admin.ModelAdmin):
	list_display = ('sender', 'subject','written','unread','id',)
	save_on_top = True
	ordering = ('-written',)



class EmailResetAdmin(admin.ModelAdmin):
	list_display = ('email', 'expires',)
	ordering = ('-expires',)
	
		

admin.site.register(Mess, MessAdmin)
admin.site.register(EmailReset, EmailResetAdmin)


