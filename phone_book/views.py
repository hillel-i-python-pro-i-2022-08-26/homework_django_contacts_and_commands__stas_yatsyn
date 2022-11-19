from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView

from phone_book.forms import AddUserForm
from phone_book.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        'name',
        'phone',
        'birthday_date',
        'avatar',
    )
    template_name_suffix = '_add_form'


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        'name',
        'phone',
        'birthday_date',
        'avatar',
    )
    template_name_suffix = '_update_form'


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('phone_book:index')


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request,
        "phone_book/index.html",
        {
            "title": "Телефонна книга",
            "contacts": contacts,
        },
    )


def search_user_info(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "phone_book/user_search.html",
        {
            "title": "Шукати користувача",
        },
    )


def show_user_search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query.startswith("0"):
        contact = Contact.objects.get(phone=query)
    else:
        contact = Contact.objects.get(pk=query)
    return render(
        request,
        "phone_book/user_info.html",
        {
            "title": f"Інформація про користувача {contact.name}",
            "contact": contact,
        },
    )


def show_user_info(request: HttpRequest, pk: Contact.pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    return render(
        request,
        "phone_book/user.html",
        {
            "title": f"Iнформація про користувача {contact.name}.",
            "contact": contact,
        },
    )
