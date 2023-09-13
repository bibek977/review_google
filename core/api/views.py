from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

class GoogleApi(views.APIView):

    def get(self,request):
        data = {
            "msg" : "Google Api Data"
        }
        return Response(data,status=status.HTTP_202_ACCEPTED)