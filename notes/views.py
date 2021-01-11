from django.shortcuts import render, redirect
from django.views import View
from .models import Note


class CreateNote(View):
    def get(self, request):
        return render(request, 'notes/create.html')

    def post(self, request):
        user = request.user
        data = request.POST
        Note.objects.create(user=user, title=data.get('title'), description=data.get('description'))

        return redirect('list_note')


class ListNote(View):
    def get(self, request):
        user = request.user
        notes = Note.objects.filter(user=user)
        return render(request, 'notes/list.html', context={'notes': notes})
