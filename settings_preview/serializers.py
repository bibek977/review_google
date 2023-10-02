from rest_framework import serializers
from .models import *

class SettingsPreviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SettingsPreview
        fields = "__all__"