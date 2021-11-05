from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from products.models import Product, Category

# Register your models here.


class ProductAdmin(ImportExportModelAdmin):
    resource_class = Product
    list_display = ("product_name", "nutriscore_grade",
                    "pnns_groups_1", "ingredients_text")
    search_fields = ("product_name", "ingredients_text")
    list_filter = ("nutriscore_grade", "pnns_groups_1")
    autocomplete_fields = ("pnns_groups_1",)


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = Category
    search_fields = ("pnns_groups_1",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
