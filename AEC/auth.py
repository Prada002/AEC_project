from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt

# from django.contrib.auth import get_user_model


from .models import *

class clientToken(BaseAuthentication):
    def authenticate(self, request):
        print("gg")
        try:
            auth_head = request.headers.get('Authorization')
            print("11")

            if auth_head:
                token = auth_head.split()[1]
                print("1")
                secret_key ="9633"
                print(21)
                payload = jwt.decode(token,secret_key,algorithms=['HS256'],verify=True)
                print("23")
                print(payload)

                request_id = payload.get('request_id')
                print("55")
                print(request_id)

                if request_id is not None:
                    a = client.objects.get(request_id=request_id)
                    print("55")
                    return a , token
                
                else:
                    raise Exception("client id is none")
                
                
            else:
                raise Exception("head is empty")
        except Exception as e :
            print('auth try except')
            raise e
        
class adminToken(BaseAuthentication):
    def authenticate(self, request):
        print(5)
        try:
            auth_head = request.headers.get('Authorization')

            print("15")

            if auth_head:
                print(7)
                token = auth_head.split()[1]
                print(8)
                secret_key ="2000"
                payload = jwt.decode(token,secret_key,algorithms=['HS256'],verify=True)
                print(9)
                admin_id = payload.get('admin_id')
                print("admin_Id",admin_id)

                if admin_id is not None:
                    a = admin.objects.get(admin_id = admin_id)
                    return a , token
                
                else:
                    raise Exception("client id is none")
                
            else:
                raise Exception("head is empty")
        except Exception as e :
            print('auth try except')
            raise e