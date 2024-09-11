from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.post_list, name = 'home'), # Home page
    path('posts/', views.post_list, name='posts'),  # Blog posts list
    path('login/', views.post_list, name='login'),  # login page
    path('register/', views.post_list, name='register'),  # registartion page

]
