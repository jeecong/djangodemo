from django.contrib import admin

# Register your models here.

from models import Publisher,Note,Browse

admin.site.register(Publisher)
admin.site.register(Note)
admin.site.register(Browse)