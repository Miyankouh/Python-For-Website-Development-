from django.contrib import admin
from django.contrib.admin import register
from catalogue.models import Category, Brand, Product, ProductAttribute, ProductAttributeValue, ProductImage, ProductType


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductAttributeValue(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'product_type', 'title',
                    'is_active', 'category', 'brand')
    list_display_links = ('title',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('upc', 'title', 'category__name', 'brand__name')
    actions = ('active_all',)
    inlines = [ProductAttributeValue, ProductImageInline]

    def active_all(self, request, queryset):
        pass

    def get_list_display(self, request):
        return self.list_display


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [ProductAttributeInline]


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type']


admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
