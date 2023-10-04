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
                           response["Access-Control-Allow-Origin"] = "*"
                           response["Access-Control-Allow-Headers"] = "*"

                           return response  
                   
                except Exception as e:
                    print(e)
                    return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})
       
    def create_record(self, request): 
            if request.method == 'POST':
                serializer = RecordSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        record = serializer.data
                        response = Response({"status": status.HTTP_201_CREATED,"message": 'successfull', "payload" : record})
                        return response
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_record(self, request, pk):
          if request.method == 'PATCH':
                try:
                      record = DigitalRoad.objects.get(pk=pk)
                except DigitalRoad.DoesNotExist:
                      return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = RecordSerializer(record, data=request.data, partial=True)
                if serializer.is_valid():
                      serializer.save()
                      return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)