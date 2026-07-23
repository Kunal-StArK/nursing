from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact

# Create your views here.

def contactview(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.objects.create(full_name=name, phone=phone, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
        return redirect('contacts')

    return render (request, 'contact.html')
