from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import Http404
from news.models import News
from news.serializer import NewsSerializer
from rest_framework.response import Response


class NewsList(generics.ListCreateAPIView):
    """
    List all news, or create a new.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a news instance.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpvote(APIView):
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        news = self.get_object(pk)
        news.upvote()
        serializer = NewsSerializer(news)
        return Response(serializer.data)
