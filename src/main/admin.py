from django.contrib import admin

from .models import Listing, LikedListing


class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)
