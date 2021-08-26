from re import T, U
from authn import serializers
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
# from django.contrib.auth.models import User
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response

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
        get_username = User.objects.filter(username=username).exists()
        if get_username:
            return Response({"error": "username already exists"})
        # RegisterSerializer.is_valid()
        # RegisterSerializer.save(data)
        else:
            User.objects.create(username=username, email=email, is_superuser=True)
            user = User.objects.get(email=email)
            user.set_password(password2)
            user.save()
            return redirect('login')
        # print(data)
        # return render(request, "authn/register.html")

class LoginApiView(APIView):
    
    def get(self, request):
        return render(request, 'authn/login.html')
    
    def post(self, request):
        req = request.POST
        username = req['username']
        password = req['password']
        user = User.objects.get(username=username)
        check_user = user.check_password(password)
        if check_user:
            return render(request, 'authn/sucess.html')
        return render(request, 'authn/login.html')
        
def logoutUser(request):
	# logout(request)
	return redirect('login')