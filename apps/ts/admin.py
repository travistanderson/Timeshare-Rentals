# ts/admin.py
from django.contrib import admin
from ts.models import Ad, Comment, Country, Email, Photoo, Resort

def approve(modeladmin, request, queryset):
	queryset.update(premod=True)
approve.short_description = "Approve Moderation"


class AdAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'resort', 'creator', 'adtype','premod','paid','expiration_date',)
	list_editable = ('premod','adtype','paid')
	list_display_links = ('name',)
	save_on_top = True
	ordering = ('-start_ad',)
	prepopulated_fields = {"slug": ("name",)}
	actions = [approve]
	
	
class PhotooAdmin(admin.ModelAdmin):
	list_display = ('id','title','date_added','orderer','ad','user','admin_thumbnail')
	list_display_links = ('title',)
	list_editable = ('orderer',)
	ordering = ('-date_added',)


class CountryAdmin(admin.ModelAdmin):
	list_display = ('id','name','iso','flag',)
	list_display_links = ('id',)
	list_editable = ('name','iso',)
	ordering = ('name',)
		
	
class ResortAdmin(admin.ModelAdmin):
	list_display = ('name', 'branch','premod','address_country',)
	prepopulated_fields = {"slug": ("name",)}
	actions = [approve]
	



admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
admin.site.register(Country, CountryAdmin)
admin.site.register(Email)
admin.site.register(Photoo,PhotooAdmin)
admin.site.register(Resort, ResortAdmin)

