# ts/admin.py
from django.contrib import admin
from ts.models import Comment, ResortType, Resort, Ad, Email, Country

class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'resort', 'creator', 'premium','premod')
    # list_filter = ['date_added', 'is_public']
    # date_hierarchy = 'date_added'
    # prepopulated_fields = {'title_slug': ('title',)}
    # filter_horizontal = ('photos',)

class ResortAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch','premod')
    # list_filter = ['date_added', 'is_public']
    # list_per_page = 10
    # prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Ad, AdAdmin)
admin.site.register(Resort, ResortAdmin)
admin.site.register(ResortType)
admin.site.register(Email)
admin.site.register(Comment)
admin.site.register(Country)