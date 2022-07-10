from django.contrib import admin
from basket.models import Basket, BasketLine
# Register your models here.


class BasketInline(admin.TabularInline):
    model = BasketLine


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']
    inlines = (BasketInline, )


admin.site.register(Basket, BasketAdmin)