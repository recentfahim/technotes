from django.contrib import admin
from django.urls import path, include
from notes.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('notes.urls')),
    path('user/', include('users.urls')),
    path('', Home.as_view(), name='home'),
]
