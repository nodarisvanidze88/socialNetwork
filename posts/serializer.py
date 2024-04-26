from rest_framework import serializers
from .models import Comments, FriendRequest, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'