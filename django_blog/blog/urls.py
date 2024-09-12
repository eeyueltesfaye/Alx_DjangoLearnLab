from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name = 'home'), # Home page
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # registration page
    path('profile/', views.profile, name='profile'),  # profile page 
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]
