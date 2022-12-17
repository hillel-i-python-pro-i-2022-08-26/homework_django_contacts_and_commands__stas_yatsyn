

from django.urls import path

from middleware import views

app_name = "middleware"

urlpatterns = [
    path("", views.MiddlewareView.as_view(), name="index"),
    path("all-info/", views.AllInfoViews.as_view(), name="all_info"),
    path("current-session/<slug:session_key>/", views.CurrentSessionInfoViews.as_view(), name="current_session_info"),
    path("current-user/<int:pk>/", views.CurrentUserInfoViews.as_view(), name="current_user_info"),
]