from django.urls import path

from . import views

app_name = "phone_book"

urlpatterns = [
    path("", views.show_contacts, name="index"),
]
