# ts/admin.py
from django.contrib import admin
from ts.models import Ad, Comment, Country, Email, Photoo, Resort

def approve(modeladmin, request, queryset):
	queryset.update(premod=True)
approve.short_description = "Approve Moderation"


class AdAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'resort', 'creator', 'adtype','premod','expiration_date',)
	list_editable = ('premod','adtype',)
	list_display_links = ('name',)
	save_on_top = True
	actions = [approve]
	
	
class PhotooAdmin(admin.ModelAdmin):
	list_display = ('id','title','date_added','orderer','ad','user','admin_thumbnail')
	list_display_links = ('title',)
	list_editable = ('orderer',)
	ordering = ('-date_added',)
	
	
class ResortAdmin(admin.ModelAdmin):
	list_display = ('name', 'branch','premod')
	actions = [approve]
	



admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(Email)
admin.site.register(Photoo,PhotooAdmin)
admin.site.register(Resort, ResortAdmin)

