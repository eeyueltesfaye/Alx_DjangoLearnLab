from django.urls import path, include 
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# Existing URL pattern for BookList view
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # for token authentication 
]


# New router for BookViewSet
router = DefaultRouter()
router.register(r'books-crud', BookViewSet)  # Use a different prefix to avoid conflict

urlpatterns += [
    path('', include(router.urls)),
]


