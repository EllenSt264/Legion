from django.contrib import admin
from .models import Category, SubCategory, FreelanceService


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'category',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'pk',
        'service_headline',
        'service_search_tags',
        'user',
    )

    ordering = ('category_name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(FreelanceService, ServiceAdmin)
