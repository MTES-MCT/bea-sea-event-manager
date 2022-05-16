from django.contrib import admin

from entry_helper.models import Report

class ReportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Report, ReportAdmin)
