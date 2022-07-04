from django.contrib import admin
from django.contrib.admin import register

from partner.models import Partner, PartnerStock


@register(PartnerStock)
class PartnerStockAdmin(admin.ModelAdmin):
    pass


@register(Partner)
class ParentAdmin(admin.ModelAdmin):
    pass