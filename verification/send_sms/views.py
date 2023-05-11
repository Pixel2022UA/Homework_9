from django.shortcuts import render, redirect, reverse
from .forms import PhoneNumberForm
from .tasks import send_sms


def send_sms_view(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            send_sms.delay(number)
            return redirect(reverse("success-page", kwargs={"phone_number": number}))
    else:
        form = PhoneNumberForm()
    context = {"form": form}
    return render(request, "send_sms.html", context)


def success_page_view(request, phone_number):
    context = {"phone_number": phone_number}
    return render(request, "success_page.html", context)
