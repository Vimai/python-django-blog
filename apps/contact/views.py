from django.shortcuts import render
from contact.forms import ContactForms


def contact(request):
    form = ContactForms()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
