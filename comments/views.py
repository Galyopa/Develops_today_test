from rest_framework import generics

from comments.models import Comment
from comments.serializer import CommentSerializer


class CommentsList(generics.ListCreateAPIView):
    """
    List all comments, or create a new.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsListFilteredByNews(generics.ListCreateAPIView):
    """
    List all comments filtered by news, or create a new.
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        news = self.kwargs['pk']
        return Comment.objects.all().filter(news=news)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
