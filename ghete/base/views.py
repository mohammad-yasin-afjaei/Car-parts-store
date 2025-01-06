from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model,authenticate,login
import json
from django.views import View


class RegisterView(View):
    def post(self, request,*args,**kwargs):
        data = json.loads(request.body)
        phone_number = data.get['phone_number']
        password = data.get['password']

        if get_user_model().objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'eror': 'Phone number already in use.'})


        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)
        return JsonResponse({'message': 'user created successfully.'})


class LoginView(View):
    def post(self,request,*args,**kwargs):
        data = json.loads(request.body)
        phone_number = data.get['phone_number']
        password = data.get['password']
        user = authenticate(request, username=phone_number, password=password)
        if user :
            login(request,user)
            return JsonResponse({'message': 'user login successfully.'})
        else:
            return JsonResponse({'message': 'invalid phone number.'})


