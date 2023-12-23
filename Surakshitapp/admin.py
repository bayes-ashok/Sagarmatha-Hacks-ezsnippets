from django.contrib import admin

from .models import Earthquake, Flood, Glof, Landslide, User

admin.site.register(User)
admin.site.register(Flood)
admin.site.register(Earthquake)
admin.site.register(Glof)
admin.site.register(Landslide)
