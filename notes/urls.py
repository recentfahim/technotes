from django.urls import path
from .views import CreateNote, ListNote, DeleteNote, EditNote, ViewNote, ShareWithMe
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/', login_required(csrf_exempt(CreateNote.as_view())), name='create_note'),
    path('list/', login_required(ListNote.as_view()), name='list_note'),
    path('delete/<int:id>', login_required(csrf_exempt(DeleteNote.as_view())), name='delete_note'),
    path('edit/<int:id>', login_required(csrf_exempt(EditNote.as_view())), name='edit_note'),
    path('view/<int:id>', login_required(csrf_exempt(ViewNote.as_view())), name='view_note'),
    path('share-with-me/', login_required(csrf_exempt(ShareWithMe.as_view())), name='share_with_me_note'),
]
