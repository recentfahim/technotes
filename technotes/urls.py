from django.contrib import admin
from django.urls import path, include
from notes.views import Home

admin.site.site_header = 'TechNote Admin'  # default: "Django Administration"
admin.site.index_title = 'TechNote Administration'  # default: "Site administration"
admin.site.site_title = 'TechNote Site Admin'  # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('notes.urls')),
    path('user/', include('users.urls')),
    path('api/v1/', include('users.api.urls')),
    path('api/v1/note/', include('notes.api.urls')),
    path('', Home.as_view(), name='home'),
]
