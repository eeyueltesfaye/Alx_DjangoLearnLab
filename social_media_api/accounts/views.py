from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer, CustomUserSerializer, UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
        })
    

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user = self.get_object()
        if request.user != user:
            request.user.following.add(user)
            return Response({'status': 'following'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        if request.user != user:
            request.user.following.remove(user)
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    


# Follow user view
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({'status': 'following'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)


# Unfollow user view
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if request.user != user_to_unfollow:
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    

