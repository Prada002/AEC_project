from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'

class clientSerializer(serializers.ModelSerializer):
    # employee_list = EmployeeSerializer(many=True,read_only=True)
    
    class Meta:
        model = client
        fields = ['client_name','client_password']
class clientSerializerget(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ["request_id",'client_name',"emp_count"]

class clientrequestSerializer(serializers.ModelSerializer):   

    class Meta:
        model = client
        fields = ["emp_count"]


class clientSerializer1(serializers.ModelSerializer):
    employee_list = EmployeeSerializer(many=True,read_only=True)
    # employee_list    = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)
    class Meta:
        model  = client
        fields = '__all__'

class adminSerializer_register(serializers.ModelSerializer):
    # office_request = serializers.PrimaryKeyRelatedField(queryset=.objects.all(), many=True)
    # employee_list    = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)

    class Meta:
        model  = admin
        fields = ['admin_id','admin_name','admin_password']

# class client_status_Serializer1(serializers.ModelSerializer):
#     selected_employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)
#     rejected_employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)
#     class Meta:
#         model = client_status
#         fields = ['client_status_id', 'request_id', 'admin_id', 'selected_employee ', 'rejected_employee']

class admin_req_Serializer(serializers.ModelSerializer):
    client_request = serializers.PrimaryKeyRelatedField(queryset=client.objects.all(), many=True)
    employee_list = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)

    class Meta:
        model  = admin
        fields = '__all__'
