from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Place,
    Image
)


class ImageInline(admin.TabularInline):
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
    list_display = ['title', 'position']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]