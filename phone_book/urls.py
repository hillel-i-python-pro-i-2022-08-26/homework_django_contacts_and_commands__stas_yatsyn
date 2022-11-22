from django.urls import path

from . import views

app_name = "phone_book"

urlpatterns = [
    path("", views.show_contacts, name="index"),
    path("add-user/", views.ContactCreateView.as_view(), name="add_user"),
    path("search-user/", views.search_user_info, name="user_search"),
    path("view-user/", views.show_user_search, name="user_info"),
    path("delete-user/<int:pk>/", views.ContactDeleteView.as_view(), name="delete_user"),
    path("user/update-user/<int:pk>/", views.ContactUpdateView.as_view(), name="update_user"),
    path("user/<int:pk>/", views.show_user_info, name="user"),
]
