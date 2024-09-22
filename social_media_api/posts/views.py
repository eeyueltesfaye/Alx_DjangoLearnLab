from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Post, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get posts from users that the current user follows
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        # Use generics.get_object_or_404 to get the Post
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Use Like.objects.get_or_create to like the post if not already liked
        like, created = Like.objects.get_or_create(user=user, post=post)

        if created:
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        # Use generics.get_object_or_404 to get the Post
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the Like exists
        like = Like.objects.filter(user=user, post=post).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)