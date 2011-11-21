# profiler/admin.py
from django.contrib import admin
from profiler.models import Mess



class MessAdmin(admin.ModelAdmin):
	list_display = ('sender', 'subject','written','unread','id',)
	save_on_top = True
	ordering = ('-written',)
	

admin.site.register(Mess, MessAdmin)


