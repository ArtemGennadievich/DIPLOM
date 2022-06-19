from django.contrib import admin
from .models import *




class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = NewGallery



class CategoryAdminSlug(admin.ModelAdmin):
    prepopulated_fields = {'cat_order_slug': ('cat_order_title',)}

class CategoryAdminSlugGlobal(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('cat_title',)}


class OrderNewAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(OrderNew, OrderNewAdmin)
admin.site.register(NewCategoryOrder, CategoryAdminSlug)
admin.site.register(NewCategory, CategoryAdminSlugGlobal)
