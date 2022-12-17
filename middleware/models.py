from django.conf import settings
from django.db import models


class Visit(models.Model):
    session_key = models.CharField(max_length=255)
    path = models.SlugField(max_length=255)
    count_of_visits = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    last_visit_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Visit Info"
