from .views import RegisterView, LoginView, UserDetailView, UserListView, UserViewSet
from django.urls import path, include 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('', include(router.urls)),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),

]
