from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('post-list/', views.PostListView.as_view(), name='post_list'),
    path('post-create/', views.PostCreateView.as_view(), name='post_create'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post-like/<int:pk>/', views.PostLikeToggleView.as_view(), name='post_like_toggle'),
    path('comment-update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
