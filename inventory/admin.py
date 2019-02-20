from django.contrib import admin
from .models import Laptop,Desktop,Mobile
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Laptop,Desktop,Mobile)
class ViewAdmin(ImportExportModelAdmin):
	list_display = ['item','price','status']
	list_filter = ['item']
	search_fields = ['item'] 
	


