from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
from .models import AdminUser


class MyUser(UserAdmin):
    add_form = UserRegistrationForm
    form = UserRegistrationForm
    model = get_user_model()
    list_display = ['email', 'password']


admin.site.register(AdminUser, MyUser)