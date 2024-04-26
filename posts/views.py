from django.shortcuts import render
from .models import Post,Comments,FriendRequest
from .serializer import CommentsSerializer, FriendSerializer, PostSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.

class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommetViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FriendRequestViewset(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LoginToken(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user = user)
            return Response({'token': token.key})
        else:
            return Response({'error':"Wrong Credentials"})
