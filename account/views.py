from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect ('dashboard')

    form = AuthenticationForm()
    data = {
        'form': form,
    }
    return render(request,'login.html',data)


def logout(request):
    auth.logout(request)
    return redirect ('home')



def dashboard(request):
    return render(request,'dashboard.html')
