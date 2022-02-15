from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import (
    Place,
    Image
)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['preview']

    def preview(self, instance: Image):
        image = instance.img

        return format_html(
            '<img src="{url}" style="max-height:150px;max-width:200px"/>',
            url=image.url
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'position']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]