"""Post URLs"""

# Django

from django.urls import path

# views
from posts.views import PostsFeedView, DetailView, new_post

urlpatterns = [
    path(
        route='',
        view=PostsFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/new/',
        view=new_post,
        name='new_post'
    ),
    path(
        route='post/<int:pk>',
        view=DetailView.as_view(),
        name='detail'
    )
]
