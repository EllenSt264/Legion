from django.contrib import admin
from .models import BasicPackage, Category, PremiumPackage, Service, StandardPackage, SubCategory, FreelanceService


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


class ServiceOldAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'pk',
        'service_headline',
        'service_search_tags',
        'user',
    )

    ordering = ('category_name',)


class BasicPackageInline(admin.StackedInline):
    model = BasicPackage
    extra = 0


class StandardPackageInline(admin.StackedInline):
    model = StandardPackage
    extra = 0


class PremiumPackageInline(admin.StackedInline):
    model = PremiumPackage
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'subcategory',
        'category',
        'pk',
        'headline',
        'user',
    )

    inline_type = 'tabular'
    inlines = [
        BasicPackageInline,
        StandardPackageInline,
        PremiumPackageInline
    ]

    ordering = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
