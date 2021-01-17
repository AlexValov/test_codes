from product.models import *
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ListItemInline(NestedStackedInline):
    model = ListItem
    extra = 1
    fk_name = 'title'


class TitleListForProductInline(NestedStackedInline):
    model = TitleListForProduct
    extra = 1
    fk_name = 'list_title'
    inlines = [ListItemInline]


class ProductAdmin(NestedModelAdmin):
    model = Product
    inlines = [TitleListForProductInline]


admin.site.register(Product, ProductAdmin)
