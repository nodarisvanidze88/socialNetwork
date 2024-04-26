from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommetViewset,PostViewsets, FriendRequestViewset,LoginToken

rout = DefaultRouter()
rout.register(r'post',PostViewsets, basename='post' )
rout.register(r'comment', CommetViewset, basename='comment')
rout.register(r'frend', FriendRequestViewset, basename="friend")

urlpatterns = [
    path('', include(rout.urls)),
    path('login/', LoginToken.as_view())
]
