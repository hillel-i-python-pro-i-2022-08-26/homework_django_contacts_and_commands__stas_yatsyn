import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


def get_user_avatar_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class AdminUser(AbstractUser):
    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_user_avatar_path,
    )

    def get_absolute_url(self):
        return reverse(
            "account:edit",
            kwargs={"pk": self.pk},
        )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Admin User"