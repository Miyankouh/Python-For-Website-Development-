from django.contrib import admin
from django.contrib.admin import register

from package.models import Package, PackageAttribute

# Register your models here.

class PackageAttributeInline(admin.TabularInline):
    model = PackageAttribute


@register(Package)
class PackageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = (PackageAttributeInline,)