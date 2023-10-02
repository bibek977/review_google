from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from .serializers import *
from .models import *


class SettingsPreviewAPI(views.APIView):

    def get(self,request):
        preview = SettingsPreview.objects.all()
        serializer = SettingsPreviewSerializer(preview,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = SettingsPreviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved'},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
    def patch(self,request,pk=None):
        id = request.data['id']
        p = SettingsPreview.objects.get(id = id)
        s = SettingsPreviewSerializer(p,data=request.data,partial=True)
        if s.is_valid():
            s.save()
            return Response({'msg':'data updated'},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({'error':s.errors},status=status.HTTP_304_NOT_MODIFIED)
