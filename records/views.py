from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import DigitalRoad
from .serializers import RecordSerializer

# Create your views here.


class RecordsViewSets(viewsets.ViewSet):
    
    def records_list(self, request):
                try:
                    if request.method == 'GET':
                           records = DigitalRoad.objects.all()
                           serializer = RecordSerializer(records, many=True)
                           result = serializer.data
                           response = Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result}, content_type ='application/json')
                           response["Access-Control-Allow-Origin"] = "*"  # Replace with the actual domain
                        #    response["Access-Control-Allow-Methods"] = "GET"
                           response["Access-Control-Allow-Headers"] = "*"

                           return response  
                   
                except Exception as e:
                    print(e)
                    return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})
       
    # def records_form(request):
    #     return
    
    # def records_delete(request):
    #     return
