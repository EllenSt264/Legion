from django.contrib import admin
from .models import FreelanceService


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_category',
        'service_headline',
        'service_search_tags',
        'user',
    )

    ordering = ('service_category',)


admin.site.register(FreelanceService, ServiceAdmin)
