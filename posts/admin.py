from django.contrib import admin
from .models import Comments, FriendRequest,Post
# Register your models here.

admin.site.register([Comments,FriendRequest,Post])