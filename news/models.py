from django.db import models


class News(models.Model):
    title = models.CharField(max_length=140)
    link = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=64)

    class Meta:
        ordering = ["-creation_date"]

    def upvote(self):
        self.amount_of_upvotes += 1
        self.save()

    def __str__(self):
        return self.title
