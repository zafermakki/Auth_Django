from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
    PermissionsMixin,
    Permission,Group
)
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid

class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key= True,
        editable= False,
        default= uuid.uuid4
    )
    username = models.EmailField(
        max_length= 250,    
        validators= [UnicodeUsernameValidator],
        unique= True
    )
    email = models.EmailField(
        max_length= 250,
        unique= True
    )
    groups = models.ManyToManyField(
        Group, related_name= 'users', related_query_name= 'user' 
    )
    Permissions = models.ManyToManyField(
        Permission, related_name= 'users', related_query_name= 'user' 
    )
    
    is_superuser = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(
        auto_now_add= True
    )
    is_client = models.BooleanField(default= False)
    
    objects = UserManager()
    
    REQUIRED_FIELDS = [
        'email'
    ]
    
    USERNAME_FIELD = 'username'
    
    class Meta:
        db_table = "users"