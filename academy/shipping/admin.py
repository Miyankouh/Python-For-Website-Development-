from django.contrib import admin
from django.contrib.admin import register
from shipping.models import ShippingAddress

# Register your models here.
@register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'zipcode', 'created_time']
