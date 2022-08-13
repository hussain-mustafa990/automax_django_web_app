from django.contrib import admin

from .models import Profile, Location


class ProfileAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)
