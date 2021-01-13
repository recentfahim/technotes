from django.urls import path
from notes.api.views import ListNote, CreateNote, NoteDetails, ShareWithMe, ShareWithOther
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('list-note/', ListNote.as_view()),
    path('create-note/', csrf_exempt(CreateNote.as_view())),
    path('note-details/<int:id>/', csrf_exempt(NoteDetails.as_view())),
    path('shared-with-me/', ShareWithMe.as_view()),
    path('share/<int:id>/', csrf_exempt(ShareWithOther.as_view())),
]
