from django.urls import path
from notes.api.views import ListNote

urlpatterns = [
    path('list-note/', ListNote.as_view())

]
