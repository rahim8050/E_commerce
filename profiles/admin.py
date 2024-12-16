from django.contrib import admin

# Register your models here.
admin.site.site_header = 'Profile'
admin.site.site_title = 'profile'
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['content','user']
    search_fields = ['content','bio']
    list_filter = ['user']
    list_per_page = 25
admin.site.register(Profile,ProfileAdmin)