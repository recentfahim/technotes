from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, authentication
from notes.models import Note
from notes.api.serializers import NoteSerializer
from guardian.shortcuts import assign_perm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ListNote(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        notes = Note.objects.filter(user=user)
        if notes:
            note_serializer = NoteSerializer(notes, many=True)

            context = {
                'data': note_serializer.data,
                'success': True
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'data': None,
                'success': False
            }

            return Response(context, status=status.HTTP_204_NO_CONTENT)


class CreateNote(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        note = Note.objects.create(user=user, title=data.get('title'), description=data.get('description'))
        assign_perm('notes.view_note', user, note)
        assign_perm('notes.change_note', user, note)
        assign_perm('notes.delete_note', user, note)
        if note:
            note_serializer = NoteSerializer(note)

            context = {
                'data': note_serializer.data,
                'success': True,
                'message': 'List Created Successfully',
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'data': None,
                'success': False,
                'message': "Couldn't create list",
            }

            return Response(context, status=status.HTTP_204_NO_CONTENT)


class NoteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note and user.has_perm('notes.change_note', note):
            note_serializer = NoteSerializer(note)

            context = {
                'data': note_serializer.data,
                'success': True,
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'data': None,
                'success': False,
                'message': "You don't have permission to view this note",
            }

            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note and user.has_perm('notes.change_note', note):
            note.title = data.get('title')
            note.description = data.get('description')
            note.save()
            note_serializer = NoteSerializer(note)

            context = {
                'data': note_serializer.data,
                'success': True,
                'message': "List Edited Successfully",
            }

            return Response(context, status=status.HTTP_200_OK)

        else:
            context = {
                'data': None,
                'success': False,
                'message': "You don't have permission to edit this note",
            }

            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        user = request.user
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note and user.has_perm('notes.delete_note', note):
            note.delete()
            context = {
                'data': None,
                'success': True,
                'message': 'List Deleted Successfully',
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'data': None,
                'success': False,
                'message': "You don't have the permission to delete this list",
            }

            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


class ShareWithMe(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        notes = Note.objects.all().exclude(user=user)
        shared_notes = []
        for note in notes:
            if user.has_perm('notes.view_note', note):
                shared_notes.append(note)
        if shared_notes:
            note_serializer = NoteSerializer(shared_notes, many=True)

            context = {
                'data': note_serializer.data,
                'success': True
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'data': None,
                'success': False
            }

            return Response(context, status=status.HTTP_204_NO_CONTENT)


class ShareWithOther(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        note = Note.objects.filter(user=user, id=kwargs.get('id')).first()
        if note:
            shared_user = UserModel.objects.filter(email=data.get('email')).first()
            if shared_user:
                assign_perm('notes.view_note', shared_user, note)
                note_serializer = NoteSerializer(note)
                context = {
                    'data': note_serializer.data,
                    'success': False,
                    'message': "Share with " + shared_user.email + " successfully",
                }

                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {
                    'data': None,
                    'success': False,
                    'message': "The user doesn't exist",
                }

                return Response(context, status=status.HTTP_204_NO_CONTENT)

        else:
            context = {
                'data': None,
                'success': False,
                'message': "The note doesn't exist",
            }

            return Response(context, status=status.HTTP_204_NO_CONTENT)
