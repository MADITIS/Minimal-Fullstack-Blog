from django.db import models
from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()
class Blog(models.Model):
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    title  = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to="images", default="images/default.jpg")
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    