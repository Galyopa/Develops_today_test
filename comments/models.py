from django.db import models

from news.models import News


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=64)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return self.author_name
