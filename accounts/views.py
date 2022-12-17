from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from admin_users.forms import UserRegistrationForm
from admin_users.models import AdminUser


class SingUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("base:index")
    template_name = "signup.html"

    class Meta:
        model = AdminUser
        fields = (
            'username',
            'avatar',
        )


class UserUpdateView(UpdateView):
    model = AdminUser
    fields = (
        "username",
        "avatar",
    )
    template_name = "user_update_form.html"
    template_name_suffix = "_update_form.html"
    success_url = reverse_lazy("base:index")
