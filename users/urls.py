from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .views import Login, Register, LogOut


urlpatterns = [
    path('login/', csrf_exempt(Login.as_view()), name='login'),
    path('register/', csrf_exempt(Register.as_view()), name='register'),
    path('logout/', login_required(LogOut.as_view()), name='logout'),
]
