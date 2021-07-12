from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','stock','category','modified_date')
    list_display_links = ('id','product_name',)
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)
