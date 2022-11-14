from django import forms
from django.core.exceptions import ValidationError

from core import settings
from .models import Contact


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birthday_date"].input_formats = settings.DATE_INPUT_FORMATS
        self.fields["birthday_date"].help_text = "Формат: dd.mm.YYYY"
        self.fields["phone"].help_text = "Введіть номер телефону починаючи з 0..."

    class Meta:
        model = Contact
        fields = ("name", "phone", "birthday_date")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdecimal():
            raise ValidationError("Номер має бути тільки цифрами!")
        elif len(phone) != 10:
            raise ValidationError("Номер не дійсний. Введіть український номер, який починається на 0")
        elif not phone.startswith("0"):
            raise ValidationError('Телефонний номер має починатись на "0"')
        return phone
