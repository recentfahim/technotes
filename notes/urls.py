from django.urls import path
from .views import CreateNote, ListNote
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('create/', csrf_exempt(CreateNote.as_view()), name='create_note'),
    path('list/', csrf_exempt(ListNote.as_view()), name='list_note'),
]
