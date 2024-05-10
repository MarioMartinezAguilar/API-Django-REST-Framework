from django.urls import path
from .views import ListUser,UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', ListUser.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),

]
