import uuid

from django.db import models


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"animals/animal/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    birthday_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)
    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    def __str__(self):
        return f"{self.name} : {self.birthday_date} : {self.phone}"

    __repr__ = __str__

    class Meta:
        ordering = ["-create_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Phone Book"
