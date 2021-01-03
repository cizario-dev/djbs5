from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'subject', 
            'gender', 
            'first_name', 
            'last_name', 
            'organization',
            'job_title', 
            'phone',
            'email', 
            'message', 
            'subscribe', 
            'cc_myself',
        )
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select rounded-0 shadow-none'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'First Name *', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Last Name *', 'autocomplete': 'off'}),
            'organization': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Company / organization', 'autocomplete': 'off'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Job title : CEO, CTO, Software Engineer, Trainee ..', 'autocomplete': 'off'}),
            'phone': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Phone *', 'autocomplete': 'off'}),
            'email': forms.TextInput(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'E-mail *', 'autocomplete': 'off'}),
            'message': forms.Textarea(attrs={'class': 'form-control rounded-0 shadow-none', 'placeholder': 'Message *', 'autocomplete': 'off'}),
            'subscribe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cc_myself': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
