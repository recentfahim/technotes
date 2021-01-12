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


class DeleteNote(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        note.delete()

        return redirect('list_note')


class EditNote(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        context = {
            'note': note
        }

        return render(request, 'notes/create.html', context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        note.title = data.get('title')
        note.description = data.get('description')
        note.save()

        return redirect('list_note')


class ViewNote(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(id=kwargs.get('id')).first()
        context = {
            'note': note
        }

        return render(request, 'notes/view.html', context=context)

