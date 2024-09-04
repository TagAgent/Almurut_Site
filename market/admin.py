from django.contrib import admin
from django.utils.html import mark_safe

from market.models import Product, ProductCategory, ProductGallery


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductGalleryInLineAdmin(admin.StackedInline):
    model = ProductGallery
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview_image_tag',)
    search_fields = ('name',)
    inlines = [ProductGalleryInLineAdmin]

    def preview_image_tag(self, obj):
        if obj.preview_image:
            return mark_safe(f'<img src="{obj.preview_image.url}" width="50" height="50" />')
        return "Нет изображения"

    preview_image_tag.short_description = 'Изображение'
