from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Messages, Product, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'category', 'description', 'image', 'show_image']

    def show_image(self, img_obj):
        if img_obj.image:
            return mark_safe('<img src={} width=70px/>'.format(img_obj.image.url))
        return None

    show_image.__name__ = "Image"


class MessagesAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "text"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MessagesAdmin)

