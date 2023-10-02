from django.urls import path
from .views import *

urlpatterns = [
    path('',SettingsPreviewAPI.as_view(),name="settings_api")
]