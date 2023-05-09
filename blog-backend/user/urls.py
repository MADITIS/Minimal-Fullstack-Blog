from django.urls import path
from .views import UserView, UsersView, CreateUserView, DeleteUserView, LoginUser

urlpatterns = [
    path("users/", UsersView.as_view(), name="users"),
    path("users/<int:pk>/", UserView.as_view(), name="user"),
    path("users/create/", CreateUserView.as_view(), name="create"),
    path("users/delete/", DeleteUserView.as_view(), name="delete"),
    path("users/login/", LoginUser.as_view(), name="login"),
]
