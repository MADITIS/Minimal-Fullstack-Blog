from ast import Delete
from django.urls import path
from .views import BlogsView, CreateBlog, UserBlogs, DeleteBlog


urlpatterns = [
    path("blogs/", BlogsView.as_view(), name='blogs'),
    path("blogs/create/", CreateBlog.as_view(), name='create-blog'),
    path("blogs/<int:id>/blogs", UserBlogs.as_view(), name='user-blogs'),
    path("blogs/delete/", DeleteBlog.as_view(), name='delete-blogs'),
]