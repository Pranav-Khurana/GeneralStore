from django.contrib import admin
from .models import item

# Register your models here.
class itemAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'price')
    search_fields = ['name']

admin.site.register(item, itemAdmin)