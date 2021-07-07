from django.contrib import admin
from .models import Product, Bill, ProductImage


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class AdminProductDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', 'count_bill')
    fields = ('slug', 'title', 'desc', 'count_bill', 'price', )
    search_fields = ('title', )
    inlines = (ProductImageInLine, )


@admin.register(Bill)
class AdminBillDisplay(admin.ModelAdmin):
    pass