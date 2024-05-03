from django.urls import path, include
from .views import *

urlpatterns = [
    path ('employee',Employeeview.as_view(),name="Employee"),
    path('employee/<int:pk>',Employeeview.as_view(),name="Employee"),

    
    path ('client',clientregisterview.as_view(),name="client"),
    path('client/<int:pk>',clientregisterview.as_view(),name="client"),

    path ('client_login',clientloginView.as_view(),name="client"),

    path ('client_request',clientrequestAPIView.as_view(),name="client_request"),

    path ('client_request/<int:pk>',clientrequestAPIView.as_view(),name="client_request"),

    path('admin_register',Admin_register_view.as_view(),name="Admin_register_view"),
    path('admin_register/<int:pk>',Admin_register_view.as_view(),name="Admin_register_view"),

    path ('admin_login',adminloginview.as_view(),name="admin_login"),

    path('admin_get',adminAPIView.as_view(),name="Admin_api_view"),

 

]
