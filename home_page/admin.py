from home_page.models import *
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ParagraphForDescriptionInline(NestedStackedInline):
    model = ParagraphForDescription
    extra = 1
    fk_name = 'home_page'


class ImageForSliderInline(NestedStackedInline):
    model = ImageForSlider
    extra = 1
    fk_name = 'home_page'


class HomePageAdmin(NestedModelAdmin):
    model = HomePage
    inlines = [ParagraphForDescriptionInline, ImageForSliderInline ]


admin.site.register(HomePage, HomePageAdmin)
