from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import DigitalRoad
from .serializers import RecordSerializer
# from .forms import SignUpForm, AddRecordForm

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
                        response["Access-Control-Allow-Origin"] = "*"
                        response["Access-Control-Allow-Headers"] = "*"
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
                      response =  Response(serializer.data)
                      response["Access-Control-Allow-Origin"] = "*"
                      response["Access-Control-Allow-Headers"] = "*"
                      return response
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_publicwifi_count(self, request):
      try:
            if request.method == 'GET':
                  count = DigitalRoad.objects.filter(dsh_category= "Public Wi-Fi").count()
                  response = Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":count}, content_type ='application/json')
                  response["Access-Control-Allow-Origin"] = "*"
                  response["Access-Control-Allow-Headers"] = "*"
                  return response

      except Exception as e:
            print(e)
            return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})

    def get_publicwifi(self, request):
      try:
            if request.method == 'GET':
                  list = DigitalRoad.objects.filter(dsh_category= "Public Wi-Fi")
                  serializer = RecordSerializer(list, many=True)
                  result=serializer.data
                  response = Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result}, content_type ='application/json')
                  response["Access-Control-Allow-Origin"] = "*"
                  response["Access-Control-Allow-Headers"] = "*"
                  return response

      except Exception as e:
            print(e)
            return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})
                              
                              
    def get_lastmile_count(self, request):
      try:
            if request.method == 'GET':
                  count = DigitalRoad.objects.filter(dsh_category= 'lastmile').count()
                  response = Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":count}, content_type ='application/json')
                  response["Access-Control-Allow-Origin"] = "*"
                  response["Access-Control-Allow-Headers"] = "*"
                  return response

      except Exception as e:
            print(e)
            return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})

    def get_lastmile(self, request):
      try:
            if request.method == 'GET':
                  list = DigitalRoad.objects.filter(dsh_category= "lastmile")
                  serializer = RecordSerializer(list, many=True)
                  result=serializer.data
                  response = Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result}, content_type ='application/json')
                  response["Access-Control-Allow-Origin"] = "*"
                  response["Access-Control-Allow-Headers"] = "*"
                  return response

      except Exception as e:
            print(e)
            return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                    "message": "Error occured during implementation",
                                    "payload": None})




# def home(request):
#             records = DigitalRoad.objects.all()

#             if request.method == 'POST':
#                   username = request.POST.get('Username')
#                   password = request.POST.get('Password')

#                   user = authenticate(request, username=username, password=password)
#                   if user is not None:
#                         login(request, user)
#                         messages.success(request, "Login successful")
#                         return redirect('home')
#                   else:
#                         messages.error(request, "There was an error logging in please try again...")
#                         return redirect('home')
#             else :
#                   return render(request, 'home.html', {'records': records})
          
# def logout_user(request):
#           logout(request)
#           messages.success(request, 'You have been logged out')
#           return redirect('home')

# def register_user(request):
#       if request.method == 'POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                   form.save()
#                   #Authenticate and Login
#                   username = form.cleaned_data['username']
#                   password = form.cleaned_data['password1']
#                   user = authenticate(username=username, password=password)
#                   login(request, user)
#                   messages.success(request, 'You have successfully registered')
#                   return redirect('home')
#       else:
#             form =  SignUpForm()
#             return render(request, 'register.html', {'form': form})
      
#       return render(request, 'register.html', {'form': form})
    

# def record(request, pk):
#       if request.user.is_authenticated:
#             record = DigitalRoad.objects.get(record_id=pk)
#             return render(request, 'record.html', {'record': record})
#       else:
#             messages.error(request, "You must be logged in to access this record.")
#             return redirect('home')

# def delete_record(request, pk):
#       if request.user.is_authenticated:
#             delete_record = DigitalRoad.objects.get(record_id=pk)
#             delete_record.delete()
#             messages.success(request, "You have successfully deleted this record.")
#             return redirect('home')
#       else:
#             messages.error(request, "You must be logged in to delete this record.")
#             return redirect('home')

# def add_record(request):
#       form = AddRecordForm(request.POST or None)
#       if request.user.is_authenticated:
#             if request.method == 'POST':
#                   if form.is_valid():
#                         add_record = form.save()
#                         messages.success(request, "Record added successfully")
#                         return redirect('home')
#             return render(request, 'add_record.html', {'form': form})
#       else:
#             messages.error(request, "You're not logged in")
#             return redirect('home') 


