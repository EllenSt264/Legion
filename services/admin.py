from django.contrib import admin
from .models import FreelanceService


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'pk',
        'service_headline',
        'service_search_tags',
        'user',
    )

    ordering = ('category_name',)


admin.site.register(FreelanceService, ServiceAdmin)
