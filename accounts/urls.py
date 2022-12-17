from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SingUpView.as_view(), name="signup"),
    path("edit/<int:pk>/", views.UserUpdateView.as_view(), name="edit"),
]