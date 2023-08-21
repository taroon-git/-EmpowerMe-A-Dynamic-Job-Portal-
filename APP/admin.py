from django.contrib import admin

# Register your models here.

from . models import*

admin.site.register(UserMaster),
admin.site.register(candidate),
admin.site.register(Company)