from django.shortcuts import render, redirect
from django.views import View
from .models import Note
from django.contrib.auth import get_user_model
from guardian.shortcuts import assign_perm
from django.contrib import messages

UserModel = get_user_model()


class CreateNote(View):
    def get(self, request):
        return render(request, 'notes/create.html')

    def post(self, request):
        user = request.user
        data = request.POST
        note = Note.objects.create(user=user, title=data.get('title'), description=data.get('description'))
        assign_perm('notes.view_note', user, note)
        assign_perm('notes.change_note', user, note)
        assign_perm('notes.delete_note', user, note)
        messages.success(request, "Note created Successfully")

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
        if note and user.has_perm('notes.delete_note', note):
            note.delete()
            messages.success(request, "Note deleted Successfully")

            return redirect('list_note')
        else:
            messages.error(request, "You don't have permission to delete this note!!")
            return redirect('list_note')


class EditNote(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note and user.has_perm('notes.change_note', note):
            context = {
                'note': note
            }

            return render(request, 'notes/create.html', context=context)
        else:
            messages.error(request, "You don't have permission to edit this note!!")
            return redirect('list_note')

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        note.title = data.get('title')
        note.description = data.get('description')
        note.save()
        messages.success(request, "Note updated Successfully")

        return redirect('list_note')


class ViewNote(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(id=kwargs.get('id')).first()
        if note and user.has_perm('notes.view_note', note):
            context = {
                'note': note
            }

            return render(request, 'notes/view.html', context=context)
        else:
            messages.error(request, "You don't have permission to edit this note!!")
            return redirect('list_note')

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.POST
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note:
            shared_user = UserModel.objects.filter(email=data.get('email')).first()
            if shared_user:
                assign_perm('notes.view_note', shared_user, note)
                messages.success(request, "Share with " + shared_user.email + " successfully")
                return redirect('list_note')
            else:
                messages.error(request, "User email doesn't exist!!")
                return redirect('view_note', id=note.id)

        else:
            messages.error(request, "Note not found!!")
            return redirect('list_note')


class ShareWithMe(View):
    def get(self, request):
        user = request.user
        notes = Note.objects.all().exclude(user=user)
        shared_notes = []
        for note in notes:
            if user.has_perm('notes.view_note', note):
                shared_notes.append(note)

        context = {
            'notes': shared_notes
        }

        return render(request, 'notes/share_with_me.html', context=context)


class Home(View):
    def get(self, request):
        return render(request, 'home.html')
