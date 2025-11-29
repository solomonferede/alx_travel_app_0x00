from django.contrib import admin
from .models import Listing, Booking, Review

# Simple registration
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Review)
