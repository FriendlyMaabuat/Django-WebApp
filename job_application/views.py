from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render

from .forms import ApplicationForm
from .models import Form


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = (
                f"Thank you for your submission, {first_name}. \n"
                f"Here are your data that has been submitted \n"
                f"First Name: {first_name}\n"
                f"Last Name: {last_name}\n"
                f"Available start date: {date}\n"
                f"Occupation: {occupation.capitalize()}\n"
                f"We will contact you soon!"
            )
            email_message = EmailMessage(
                "Form submission confirmation", message_body, to=[email]
            )
            email_message.send()

            messages.success(
                request,
                "Form submitted successfully. We will contact you soon. Thank you!",
            )
    return render(request, "index.html")
