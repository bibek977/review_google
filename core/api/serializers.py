from rest_framework import serializers
from core.models import *

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviewer
        fields = "__all__"