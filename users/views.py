from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


UserModel = get_user_model()


class Login(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = authenticate(request, username=data.get('email'), password=data.get('password'))
        if user:
            login(request, user)
            return redirect('list_note')
        else:
            return redirect('login')


class Register(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        if UserModel.objects.filter(username=data.get('username'), email=data.get('email')).exists():
            return redirect('register')
        user = UserModel.objects.create_user(data.get('username'), data.get('email'), data.get('password'))
        if user:
            login(request, user)
            return redirect('list_note')
        else:
            return redirect('register')

