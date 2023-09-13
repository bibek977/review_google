from django.contrib import admin
from .models import *

class CompanyModelAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "title",
        "rate",
        "person"
    ]

class ReviewerModelAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "star",
        "date"
    ]

admin.site.register(Company,CompanyModelAdmin)
admin.site.register(Reviewer,ReviewerModelAdmin)