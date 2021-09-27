from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from products.models import Product, Category

# Register your models here.
class ProductAdmin(ImportExportModelAdmin):
     resource_class = Product

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
