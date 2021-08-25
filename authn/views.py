from authn import serializers
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
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

    def get(self, request):
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
    
    def post(self, request):
        req = request.POST
        username = req['username']
        email = req['email']
        password1 = req['password1']
        password2 = req['password2']
        data = {'username': username, 'email': email, 'password1': password1, 'password2': password2}
        # RegisterSerializer.is_valid(raise_exception=True)
        # User.save(data)
        print(data)
        return render(request, "authn/register.html")