from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets 
from django.contrib.auth.hashers import check_password,make_password

# from jwt import encode
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .auth import *
import jwt
from rest_framework import permissions
from rest_framework import status


# from django.http import HttpResponse
# Create your views here.


class Employeeview(APIView):
    
     # def get(self, request,pk="none"):
     #    try:
     #        if pk:
     #            employee=Employee.objects.get(pk=pk)
     #            serializer = EmployeeSerializer(employee)
     #            return Response({"data":serializer.data},status=status.HTTP_200_OK)
     #        else:
     #            employe_data = Employee.objects.all().order_by('pk')
     #            serializer = EmployeeSerializer(employe_data,many=True)
     #            return Response({"data":serializer.data},status=status.HTTP_200_OK)
     #    except Employee.DoesNotExist:
     #        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
     #    except Exception as e:
     #        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
     def get(self, request):
        try:
            queryset = Employee.objects.all().order_by('pk')
            serializer = EmployeeSerializer(queryset,many=True)
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     def post(self, request):
          try:
               serializers = EmployeeSerializer(data=request.data)
               if serializers.is_valid():
                    serializers.save()
                    return Response({"data":serializers.data},status=status.HTTP_201_CREATED)
               else:
                    return Response ({"warning":serializers.errors},status=status.HTTP_400_BAD_REQUEST)
          except Exception as e:
               print(e)
               return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          

     def put(self,request,pk):
          try:
              employee_data = Employee.objects.get(pk=pk)
              print(employee_data)
              serializer = EmployeeSerializer(employee_data,data=request.data,partial=True)
              if serializer.is_valid():
                   serializer.save()
                   return Response({"msg":"updated","data":serializer.data},status=status.HTTP_200_OK)
              else :
                   return Response ({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
          except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
          except Exception as e :
              print(e)
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
     def delete(self,request,pk):
         try:
              a = Employee.objects.get(pk=pk)
              a.delete()
              return Response({"deleted"},status=status.HTTP_200_OK)
         except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
         except Exception as e :
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

class clientregisterview(APIView):
     def get(self, request):
        try:
            queryset = client.objects.all().order_by('pk')
            serializer = clientSerializerget(queryset,many=True)
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          

     def post(self, request):
          try:
               request.data['client_password'] = make_password(request.data['client_password'])
               serializer = clientSerializer(data=request.data)
               if serializer.is_valid():
                    serializer.save()
                    return Response({"registered":serializer.data},status=status.HTTP_200_OK)
               else:
                    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
          except Exception as e:
               print(e)
               return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


     def put(self,request,pk):
         try:
              a = client.objects.get(pk=pk)
              serializer = clientSerializer(a,data=request.data,partial=True)
              if serializer.is_valid():
                   serializer.save()
                   return Response({"msg":"updated","data":serializer.data},status=status.HTTP_200_OK)
              else :
                   return Response ({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
         except client.DoesNotExist:
               return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
         except Exception as e :
              print(e)
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
     def delete(self,request,pk):
         try:
              a = client.objects.get(pk=pk)
              a.delete()
              return Response({"deleted"},status=status.HTTP_200_OK)
         except client.DoesNotExist:
              return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
         except Exception as e :
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
class clientloginView(APIView):
    def post(self, request):
        try:
            client_name = request.data.get('client_name')
            client_password = request.data.get('client_password')

            x = client.objects.get(client_name=client_name)
            if x and check_password(client_password, x.client_password):
                payload = {
                    "request_id": x.request_id,
                    "client_name": x.client_name,
                    "client_password": x.client_password
                }
                secret_key = "9633"
                print(payload)

                token = jwt.encode(payload, secret_key, algorithm="HS256")
                return Response({"payload": payload, "token": token},status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except client.DoesNotExist:
            return Response({"error": "Client does not exist"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)  
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class clientrequestAPIView(APIView):
     authentication_classes=[clientToken,]

     def post(self,request):
          try:
               emp_count=request.data['emp_count']
               print(emp_count)
               print("22")
               a=client.objects.get(request_id=emp_count)

               serializers=clientrequestSerializer(a,request.data,partial=True)
               if serializers.is_valid():
                    serializers.save()
                    return Response({"registered":serializers.data},status=status.HTTP_200_OK)

               else:
                    return Response({"error":serializers.errors},status=status.HTTP_400_BAD_REQUEST)
          except client.DoesNotExist:
               return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
          except ValueError as e:
               print(e)
               return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
               
          except Exception as e:
               print(e)
               return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     def get(self, request):
        try:
            request_id = request.user.request_id
            queryset = client.objects.filter(request_id=request_id)
            serializer = clientSerializer1(queryset,many=True)
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     def put(self,request,pk):
         try:
              a = client.objects.get(pk=pk)
              serializer = clientrequestSerializer(a,data=request.data,partial=True)
              if serializer.is_valid():
                   serializer.save()
                   return Response({"msg":"updated","data":serializer.data},status=status.HTTP_200_OK)
              else :
                   return Response ({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
         except client.DoesNotExist:
               return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

         except Exception as e :
              print(e)
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
     def delete(self,request,pk):
         try:
              a = client.objects.get(pk=pk)
              pass
              return Response({"deleted"},status=status.HTTP_200_OK)
         except Exception as e :
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   
class Admin_register_view(APIView):
     def get(self, request):
        try:
            queryset = admin.objects.all().order_by('pk')
            serializer = adminSerializer_register(queryset,many=True)
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          

     def post(self, request):
          try:
               request.data['admin_password'] = make_password(request.data['admin_password'])
               serializer = adminSerializer_register(data=request.data)
               if serializer.is_valid():
                    serializer.save()
                    return Response({"registered":serializer.data},status=status.HTTP_200_OK)
               else:
                    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
          except Exception as e:
               print(e)
               return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


     def put(self,request,pk):
         try:
              a = admin.objects.get(pk=pk)
              serializer = adminSerializer_register(a,data=request.data,partial=True)
              if serializer.is_valid():
                   serializer.save()
                   return Response({"msg":"updated","data":serializer.data},status=status.HTTP_200_OK)
              else :
                   return Response ({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
         except admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
         except Exception as e :
              print(e)
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
     def delete(self,request,pk):
         try:
              a = admin.objects.get(pk=pk)
              a.delete()
              return Response({"deleted"},status=status.HTTP_200_OK)
         except admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
         except Exception as e :
              return Response ({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
class adminloginview(APIView):
     def post(self,request):
          try:
               admin_name=request.data.get('admin_name')
               admin_password=request.data.get('admin_password')

               x=admin.objects.get(admin_name=admin_name)
               if x and check_password(admin_password,x.admin_password):
                    payload={
                         "admin_id":x.admin_id,
                         "admin_name":x.admin_name,
                         "admin_password":x.admin_password
                    }
                    secret_key="2000"
                    token=jwt.encode(payload,secret_key,algorithm="HS256")
                    return Response({"payload": payload, "token": token}, status=status.HTTP_200_OK)
               else:
                return Response({"error": "Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
          except admin.DoesNotExist:
               return Response({"error": "admin does not exist"}, status=status.HTTP_404_NOT_FOUND)
          except Exception as e:
               return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class adminAPIView(APIView):
     authentication_classes=[adminToken,]
     def get(self,request):
          print(3)
          try:
            admin_id = request.user.admin_id
            request1=client.objects.filter(admin_id=admin_id)
            serializer = clientSerializerget(request1,many=True)
            return Response({"data":serializer.data})
            print(admin_id)
          except Exception as e:
            return Response({"error": str(e)})
          
     def post(self,request):
          try:
               client_request=request.data['client_request']
               employee_list=request.data['employee_list']
               admin_id=request.user.admin_id
               admin1=admin.objects.get(admin_id=admin_id)
               serializers=admin_req_Serializer(admin1,data=request.data,partial=True)
               if serializers.is_valid():
                    serializers.save()
                    print(5)
                    # return Response({"registered":serializers.data})
                    request_id=client_request[0]
                    client1=client.objects.get(request_id=request_id)
                    print("tg1")
                    client1.employee_list.set(employee_list)
                    serializers1=clientSerializer1(client1,data=request.data,partial=True)
                    if serializers1.is_valid():
                         serializers1.save()
                         print("rh2")
                         return Response({"registered":serializers.data},{"registered":serializers1.data},tatus=status.HTTP_200_OK)
                    else:
                         return Response({"error":serializers1.errors},status=status.HTTP_400_BAD_REQUEST)
                    # print("req_ID",request_id)
                    
               

               else:
                    return Response({"error":serializers.errors},status=status.HTTP_400_BAD_REQUEST)
               
               print(client_request)
               print(employee_list)
          except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)





         

         
     