
# Register your models here.
from django.contrib import admin
from .models import Product, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

