from requests import delete
from rest_framework import status
from backend.response import _Response
from rest_framework.views import APIView


from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from .models import Blog
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import BlogSerializer, CreateBlogSerializer

User = get_user_model()

class BlogsView(APIView):
    def get(self, *kwargs):
        blogsQS = Blog.objects.all().order_by('-date_added')

        if not blogsQS:
            return _Response(status=status.HTTP_204_NO_CONTENT, message="No Blogs")
        blogs = BlogSerializer(blogsQS, many=True).data
        return _Response(data=blogs, status=status.HTTP_200_OK, message="Request Was successful")


class CreateBlog(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        form_data = request.data
        title = form_data.get('title') or None
        content = form_data.get('content') or None
        image = form_data.get('image') or None

        if not title or not content or not image:
            return _Response(data={
                'status': False,
                'message': "One or More empty fields",
                },
                status=status.HTTP_400_BAD_REQUEST,
                message="Invalid field data"
            )


        print(form_data.get("author"),request.FILES.get("image"), type(form_data.get("author")))
        try:
            user = User.objects.get(pk=form_data.get("author"))
        except User.DoesNotExist:
            return _Response(data={"status": False,
                                   "message": "User Does not exist"
                                   },
                                   status=status.HTTP_404_NOT_FOUND,
                                   message="Invalid user ID"        
                            )
                
        blog = Blog(
            author=user,
            title=title,
            content=content,
            image=image,
        )
        blog.save()
        return _Response({"status": True, "message": "Blog created successfully"}, status=status.HTTP_200_OK, message="Request successful")
    

class UserBlogs(APIView):
    def get(self, request, id):

        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return _Response(
                data={
                    "status": False,
                    "message": "User does not exist",
                },
                status=status.HTTP_404_NOT_FOUND,
                message="Invalid User"
            )

        blogs = Blog.objects.filter(author=user)

        if blogs:
            data = BlogSerializer(blogs, many=True).data
            return _Response(
                data={
                    "status": True,
                    "data": data,
                },
                status=status.HTTP_200_OK,
                message="Request successful"
            )
        return _Response(
            data={
                "status": False,
                "message": "No Content", 
            },
            status=status.HTTP_204_NO_CONTENT,
            message="No content"
        )

class DeleteBlog(APIView):
    def delete(self, request):
        blogID = request.data.get("blogID")
        userID = request.data.get("userID")

        try:
            user = User.objects.get(pk=userID)
        except User.DoesNotExist:
            return _Response(
                data={
                    "status": False,
                    "message": "User does not exist",
                },
                status=status.HTTP_404_NOT_FOUND,
                message="Invalid User"
            )

        try:
            blog = Blog.objects.get(pk=blogID, author=user)
        except Blog.DoesNotExist:
            return _Response(
                data={
                    "status": False,
                    "message": "Blog does not exist",
                },
                status=status.HTTP_404_NOT_FOUND,
                message="Invalid User"
            )

        blog.delete()

        return _Response(data={
            "status":True,
            "message": "Delete successful",
            },
            status=status.HTTP_200_OK,
            message="Request successful"
        )