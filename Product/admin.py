from django.contrib import admin

# Register your models here.
admin.site.site_header = 'Products'
admin.site.site_title = 'products'
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['content','price']
    search_fields = ['content','price']
    list_filter = ['price']
    list_per_page = 25
admin.site.register(Product,ProductAdmin)