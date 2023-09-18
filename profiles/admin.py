from django.contrib import admin
from .models import UserProfile


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )


admin.site.register(UserProfile, AccountAdmin)

