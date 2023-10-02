from django.contrib import admin
from .models import *

class SettingsPreviewAdmin(admin.ModelAdmin):
    list_display = ['previewId','ShowReviewersName']

admin.site.register(SettingsPreview,SettingsPreviewAdmin)