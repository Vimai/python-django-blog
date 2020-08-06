from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='email', max_length=255)
    message = forms.CharField(label='message', max_length=255)
