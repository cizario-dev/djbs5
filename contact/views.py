from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Your contact has been successfully received! We will be in touch shortly.')
            return redirect(reverse_lazy('contact:index'))
        else:
            messages.error(request, 'Please correct the errors below.')
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ContactForm()

    context = {'form': form}    
    return render(request, 'contact/index.html', context)
    
