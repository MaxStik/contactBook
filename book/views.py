from django.shortcuts import render
from .forms import ContactBookForm, EditContactForm
from django.http import JsonResponse
from .models import Contact
import datetime

def main_page(request):
    form = ContactBookForm()
    edit_form = EditContactForm()
    contacts = Contact.objects.all()
    data = {
        'form': form,
        'contacts': contacts,
        'edit_form': edit_form,
    }
    return render(request,'index.html', data)


def add_contact(request):
    if request.is_ajax():
        name = request.GET.get('name', None)
        surname = request.GET.get('surname', None)
        middle_name = request.GET.get('middle_name', None)
        email = request.GET.get('email', None)
        phone = request.GET.get('phone', None)
        birthday = request.GET.get('birthday', None)

        if name and surname and middle_name and email and phone and birthday is not None:
            contact = Contact()
            contact.name = name
            contact.surname = surname
            contact.middle_name = middle_name
            contact.email = email
            contact.phone = phone
            contact.birthday = birthday
            contact.save()
            contact_id = contact.id
            data = {
                'added': True,
                'fio': surname + " " + surname + " " + middle_name,
                'email': email,
                'phone': phone,
                'birthday': birthday,
                'contact_id': contact_id,
            }
            return JsonResponse(data)
        else:
            data = {
                'added': False,
            }
            return JsonResponse(data)


def get_contact(request):
    if request.is_ajax():
        contact_id = request.GET.get('contact_id', None)
        if contact_id is not None:
            contact = Contact.objects.get(pk=contact_id)
            data = {
                'error': False,
                'name': contact.name,
                'surname': contact.surname,
                'middlename': contact.middle_name,
                'email': contact.email,
                'phone': contact.phone,
                'birthday': contact.birthday,
                'contact_id': contact.id
            }
            return JsonResponse(data)
        else:
            data = {
                'error': True,
                'erro_message': 'Нет такого контакта',
            }
            return JsonResponse(data)


def delete_contact(request):
    if request.is_ajax():
        contact_id = request.GET.get('contact_id', None)
        if contact_id is not None:
            contact = Contact.objects.get(pk=contact_id)
            contact.delete()
            data = {
                'error': False,
                'contact_id': contact_id
            }
            return JsonResponse(data)
        else:
            data = {
                'error': True,
                'erro_message': 'Нет такого контакта',
            }
            return JsonResponse(data)

def edit_contact(request):
    if request.is_ajax():
        name = request.GET.get('name', None)
        surname = request.GET.get('surname', None)
        middle_name = request.GET.get('middle_name', None)
        email = request.GET.get('email', None)
        phone = request.GET.get('phone', None)
        birthday = request.GET.get('birthday', None)
        contact_id = request.GET.get('contact_id', None)
        try:
            contact = Contact.objects.get(pk=contact_id)
            if name is not None:
                contact.name = name
            if surname is not None:
                contact.surname = surname
            if middle_name is not None:
                contact.middle_name = middle_name
            if email is not None:
                contact.email = email
            if phone is not None:
                contact.phone = phone
            if birthday is not None:
                birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                contact.birthday = birthday
            contact.save()
            data = {
                'error': False,
                'name': contact.name,
                'surname': contact.surname,
                'middlename': contact.middle_name,
                'email': contact.email,
                'phone': contact.phone,
                'birthday': contact.birthday,
                'contact_id': contact.id,
            }
            return JsonResponse(data)
        except Contact.DoesNotExist:
            data = {
                'error': True,
                'erro_message': 'Нет такого контакта',
            }
            return JsonResponse(data)