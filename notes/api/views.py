from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, authentication


class ListNote(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = request.user
        context = {
            'notes': None
        }
        return Response(context, status=status.HTTP_200_OK)
