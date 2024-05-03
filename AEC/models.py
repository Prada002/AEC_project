from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True,unique=True)
    emp_name = models.CharField(max_length=100) 
    emp_age=models.IntegerField()
    emp_role = models.CharField(max_length=100) 

class client(models.Model) :  
    request_id   = models.AutoField(primary_key=True,default=None)
    emp_role  = models.CharField(max_length=100,default=None,null=True)
    emp_count = models.IntegerField(default=0,null=True)
    client_name = models.CharField(max_length=100,unique=True)
    client_password=models.CharField(max_length=100,default=None,null=True)
    admin_id = models.ForeignKey('admin',on_delete=models.DO_NOTHING,default=None,null=True)
    employee_list = models.ManyToManyField("Employee",default=None)

class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100,unique=True)
    admin_password = models.CharField(max_length=100, default=None)
    client_request = models.ManyToManyField("client",default=None)
    employee_list = models.ManyToManyField("Employee",default=None)






