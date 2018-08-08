from django import forms
from .models import Contact


class ContactBookForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name',
            'surname',
            'middle_name',
            'email',
            'phone',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'datepicker-field'}),
        }


class EditContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name',
            'surname',
            'middle_name',
            'email',
            'phone',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'edit-datepicker-field'}),
        }