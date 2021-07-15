from django.contrib import admin
from .models import Product,Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','stock','category','modified_date')
    list_display_links = ('id','product_name',)
    prepopulated_fields = {'slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('id','product','variation_category','variation_value')

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
