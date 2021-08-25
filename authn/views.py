from re import T, U
from authn import serializers
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
# from django.contrib.auth.models import User
from .models import User
from rest_framework.views import APIView
# Create your views here.

def RegisterView(request):
    # print("request", request.POST['username'])
    req = request.POST
    username = req['username']
    email = req['email']
    password1 = req['password1']
    password2 = req['password2']
    data = {'username': username, 'email': email, 'password1': password1, 'password2': password2}
    # RegisterSerializer.is_valid(raise_exception=True)
    # User.save(data)
    print(data)
    return render(request, 'authn/register.html')

def LoginView(request):
    print("request", request.body)
    return render(request, 'authn/login.html')

class RegisterApiView(APIView):
    # queryset = Product.objects.all().order_by('-id')
    serializer_class = RegisterSerializer

    def get(self, request):
        return render(request, 'authn/register.html')
    
    def post(self, request):
        req = request.POST
        username = req['username']
        email = req['email']
        password1 = req['password1']
        password2 = req['password2']
        data = {'username': username, 'email': email, 'password1': password1, 'password2': password2}
        # RegisterSerializer.is_valid()
        # RegisterSerializer.save(data)
        User.objects.create(username=username, email=email, password=password2, is_superuser=True)
        # print(data)
        return render(request, "authn/register.html")