from django.urls import path
from comments import views

urlpatterns = [
    path("comments/", views.CommentsList.as_view()),
    path("comment/<int:pk>/", views.CommentDetail.as_view()),
    path(
        "comments_by_news/<int:pk>/",
        views.CommentsListFilteredByNews.as_view(),
    ),
]
