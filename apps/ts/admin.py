# ts/admin.py
from django.contrib import admin
from ts.models import Ad, Comment, Country, Email, PhotoOrder, Resort, ResortType

def approve(modeladmin, request, queryset):
	queryset.update(premod=True)
approve.short_description = "Approve Moderation"


class AdAdmin(admin.ModelAdmin):
	list_display = ('name', 'resort', 'creator', 'premium','premod')
	# list_filter = ['date_added', 'is_public']
	# date_hierarchy = 'date_added'
	# prepopulated_fields = {'title_slug': ('title',)}
	# filter_horizontal = ('photos',)
	actions = [approve]

class ResortAdmin(admin.ModelAdmin):
	list_display = ('name', 'branch','premod')
	# list_filter = ['date_added', 'is_public']
	# list_per_page = 10
	# prepopulated_fields = {'title_slug': ('title',)}
	actions = [approve]
	
class ResortTypeAdmin(admin.ModelAdmin):
	list_display = ('name','premod',)
	actions = [approve]




admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(Email)
admin.site.register(PhotoOrder)
admin.site.register(Resort, ResortAdmin)
admin.site.register(ResortType, ResortTypeAdmin)
