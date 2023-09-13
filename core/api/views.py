from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from .serializers import *
from core.models import *


class GoogleApi(views.APIView):

    def get(self,request):
        company = Company.objects.all()
        serializer = CompanySerializer(company,many=True)

        review = Reviewer.objects.all()
        s = ReviewSerializer(review,many=True)
        reviewer = {
            "company" : serializer.data,
            "data" : s.data
        }
        return Response(reviewer,status=status.HTTP_202_ACCEPTED)