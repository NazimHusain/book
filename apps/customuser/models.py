
# Create your models here.
from django.db import models
from apps.helpers import models as coreModels
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from apps.customuser.managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    """Model for saving basic user info."""

    email = models.EmailField("email address", unique=True, null=True, blank=True)
    username = models.EmailField("username", unique=True)  
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    role = models.ForeignKey(
        coreModels.DropdownValues, null=True, blank=True, on_delete=models.PROTECT
    )
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
  
    profilePic = models.ForeignKey(
        coreModels.FileUpload,
        null=True,
        blank=True,
        related_name="user_profile_pic",
        on_delete=models.PROTECT,
    )
    USERNAME_FIELD = "username"
    objects = CustomUserManager()

    def __str__(self: "User") -> str:
        return str(self.username)