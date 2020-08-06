from django.shortcuts import render
from contact.forms import ContactForms


def contact(request):
    form = ContactForms()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def review(request):
    form = ContactForms()
    context = {'form': form}
    print(request.method)

    if request.method == 'POST':
        form = ContactForms(request.POST)
        context = {'form': form}

    return render(request, 'contact/review.html', context)
