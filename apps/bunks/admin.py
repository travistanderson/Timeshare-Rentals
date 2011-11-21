from django.contrib import admin
from models import Bunk

class BunkAdmin(admin.ModelAdmin):
  list_display = ('key', 'id')
  search_fields = ('key', 'content')

admin.site.register(Bunk, BunkAdmin)