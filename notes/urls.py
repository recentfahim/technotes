from django.urls import path
from .views import CreateNote, ListNote, DeleteNote, EditNote
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('create/', csrf_exempt(CreateNote.as_view()), name='create_note'),
    path('list/', csrf_exempt(ListNote.as_view()), name='list_note'),
    path('delete/<int:id>', csrf_exempt(DeleteNote.as_view()), name='delete_note'),
    path('edit/<int:id>', csrf_exempt(EditNote.as_view()), name='edit_note'),
]
