from django.urls import path, include 
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


# Existing URL pattern for BookList view
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# New router for BookViewSet
router = DefaultRouter()
router.register(r'books-crud', BookViewSet)  # Use a different prefix to avoid conflict

urlpatterns += [
    path('', include(router.urls)),
]