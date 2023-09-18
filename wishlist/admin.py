from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """wishlist admin"""
    model = Wishlist
    fields = ('user_profile', 'product')
    list_display = ('pk', 'user_profile', 'product')


admin.site.register(Wishlist, WishlistAdmin)
