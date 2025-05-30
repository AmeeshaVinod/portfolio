# portfolio/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose email
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            recipient_email = 'ameeshavinod04@gmail.com'  # Replace with your actual email

            # Send email
            try:
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [recipient_email],
                    fail_silently=False,
                )
                return redirect(reverse('index') + '?success=true')
            except Exception as e:
                form.add_error(None, f"Error sending email: {str(e)}")
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})