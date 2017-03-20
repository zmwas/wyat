from actstream.actions import action
from actstream.models import Action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

'''
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            comment = Comment.objects.create(**serializer.validated_data)

            Action.objects.create(actor=comment.user,action_object=comment,verb="commented on",target=comment.content_object)

           # action.send(request.user,action_object=comment,verb="commented on",target=comment.content_object)

            return Response(
            serializer.data, status=status.HTTP_201_CREATED
            )

        return Response({
            'status': 'Bad request',
            'message': 'Comment could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

'''