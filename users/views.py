from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


UserModel = get_user_model()


class Login(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = authenticate(request, username=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('home')
        else:
            messages.error(request, "The provided username or  password is wrong!!")
            return redirect('login')


class LogOut(View):
    def get(self, request):
        user = request.user
        if user:
            logout(request)
            messages.success(request, "Logged in Successfully!!")

            return redirect('/user/login/')
        else:
            messages.error(request, "Something went wrong!!")
            return redirect('home')


class Register(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        if UserModel.objects.filter(email=data.get('email')).exists():
            messages.error(request, "The email already exist!!")
            return redirect('register')
        user = UserModel.objects.create_user(data.get('username'), data.get('email'), data.get('password'))
        if user:
            messages.success(request, "Registered Successfully, Please login!!")
            return redirect('login')
        else:
            messages.error(request, "Something went wrong!!")
            return redirect('register')

