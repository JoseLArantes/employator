from django.contrib import admin
from . import models
from companies.models import Company, OpenPosition
from import_export.admin import ImportExportModelAdmin


class OpenPositionInline(admin.TabularInline):  # Use TabularInline or StackedInline depending on your preference
    model = OpenPosition
    extra = 1
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'type', 'url', 'rating', 'status')
    inlines = [OpenPositionInline]
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(OpenPosition)