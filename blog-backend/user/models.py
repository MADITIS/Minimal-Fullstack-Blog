from multiprocessing import Value
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if not username:
            raise ValueError("The Username must be set")
        if not password:
            raise ValueError('The Password must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=200,unique=True)

    objects = UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}'
