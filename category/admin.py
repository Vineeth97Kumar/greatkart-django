from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name',)
    list_display_links = ('category_name',)
    prepopulated_fields = {'slug' : ('category_name',)}

admin.site.register(Category,CategoryAdmin)

