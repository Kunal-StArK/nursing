from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import AdduserForm , EdituserForm, PatientRegistrationForm, PatientEditForm, AdddoctorsForm , EditdoctorsForm,EditStory,Addstory,EditStats,Addstats,RegisterForm, ForgotPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model 
User = get_user_model()
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from doctors.models import Doctors
from about.models import Story,hopitalStats
from contactUs.models import contact

#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import messages


# Login / Logout Views
def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
            except Exception as e:
                import traceback
                print(f"[REGISTRATION ERROR - form.save()] {e}")
                print(traceback.format_exc())
                messages.error(request, "Registration failed due to a server error. Please try again.")
                return render(request, 'accounts/register.html', {'form': form})

            # User Activation Email
            try:
                current_site = get_current_site(request)
                mail_subject = 'Please activate your account'
                email_body = render_to_string('accounts/account_varification_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                })
                to_email = user.email
                send_email = EmailMessage(mail_subject, email_body, to=[to_email])
                send_email.send()
                messages.success(request, "Registration Successful. Please verify your email to login.")
            except Exception as e:
                import traceback
                print(f"[REGISTRATION ERROR - email sending] {e}")
                print(traceback.format_exc())
                messages.warning(request, "Registration successful! However, we could not send the activation email. Please contact the administrator to activate your account.")
            
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully! You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return redirect('register')

def forgotpassword(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user is not None:
                current_site = get_current_site(request)
                mail_subject = 'Reset your password'
                email_body = render_to_string('accounts/reset_password_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                })
                to_email = user.email
                try:
                    send_email = EmailMessage(mail_subject, email_body, to=[to_email])
                    send_email.send()
                    messages.success(request, "Password reset link has been sent to your email.")
                except Exception as e:
                    # Print link in terminal for local testing
                    uid_str = urlsafe_base64_encode(force_bytes(user.pk))
                    if isinstance(uid_str, bytes):
                        uid_str = uid_str.decode()
                    token_str = default_token_generator.make_token(user)
                    reset_link = f"http://{current_site.domain}/account/resetpassword/{uid_str}/{token_str}/"
                    print(f"[DEVELOPMENT ONLY] Reset Link: {reset_link}")
                    messages.warning(request, "Could not send email. (For development, the reset link has been printed to the server terminal console).")
            else:
                messages.success(request, "If that email exists in our system, we have sent a password reset link.")
            return redirect('forgotpassword')
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgotpassword.html', {'form': form})

def resetpassword(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been reset successfully! You can now log in.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/resetpassword.html', {'form': form})
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('forgotpassword')
    

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are logged In')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
            form = AuthenticationForm(initial={'username': username})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged Out')
    return redirect('login')

# --- PATIENTS VIEWS ---

@login_required(login_url='login')
def dashboard(request):
    all_patients = Patient.objects.all().order_by('-created_at')
    total_patients = all_patients.count()
    confirmed_appointments = all_patients.filter(status='Confirmed').count()
    pending_appointments = all_patients.filter(status='Pending').count()

    paginator = Paginator(all_patients, 5)  # 5 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'patients': page_obj,  
        'total_patients': total_patients,
        'confirmed_appointments': confirmed_appointments,
        'pending_appointments': pending_appointments,
        'page_obj': page_obj,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def add_patient(request):  
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.added_by = request.user.username
            patient.save()
            return redirect('dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'add_patient.html', {'form': form})

@login_required(login_url='login')
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientEditForm(instance=patient)
    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

@login_required(login_url='login')  
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('dashboard')

# --- USERS VIEWS ---

@login_required(login_url='login')
def users(request):
    all_users = User.objects.all()
    paginator = Paginator(all_users, 3)  # 3 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    data = {
        'users': page_obj,  
        'page_obj': page_obj,
    }
    return render(request, 'users.html', data)

@login_required(login_url='login')
def add_user(request):
    if request.method == "POST":
        form = AdduserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AdduserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required(login_url='login')
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EdituserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EdituserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

@login_required(login_url='login')
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')

# Views for doctors
@login_required(login_url='login')
def doctorsall(request):
    all_doctor = Doctors.objects.all()
    data ={
        'all_doctor': all_doctor,
    }
    return render(request,'doctordash.html',data)

@login_required(login_url='login')
def add_doctors(request):
    if request.method == 'POST':
        form = AdddoctorsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('doctorsall')
    else:    
        form = AdddoctorsForm()
    return render(request,'add_doctors.html',{'form': form})

@login_required(login_url='login')
def edit_doctors(request,pk):
    doctor = get_object_or_404(Doctors,pk=pk)
    if request.method == 'POST':
        form = EditdoctorsForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctorsall')
    else:
        form = EditdoctorsForm(instance=doctor)        
    return render(request,'edit_doctors.html',{'form': form})

@login_required(login_url='login')
def delete_doctors(request,pk):
    doctor = get_object_or_404(Doctors,pk=pk)
    doctor.delete()
    return redirect ('doctorsall')


# views for Story
@login_required(login_url='login')
def story(request):
    story = Story.objects.all()
    return render(request,'story.html',{'story':story})

@login_required(login_url='login')
def add_story(request):
    if request.method == 'POST':
        form = Addstory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('story')
    else:
        form = Addstory ()
    return render (request,'add_story.html',{'form': form})

@login_required(login_url='login')
def edit_story(request,pk):
    story = get_object_or_404(Story,pk=pk)
    if request.method == 'POST':
        form = EditStory(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            return redirect ('story')
    else:
        form = EditStory (instance=story)
    return render(request,'edit_story.html',{'form': form})

@login_required(login_url='login')
def delete_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story.delete()
    return redirect('story')


# views for stats
@login_required(login_url='login')
def stats(request):
    stats = hopitalStats.objects.all()
    return render(request,'stats.html',{'stats':stats})

@login_required(login_url='login')
def add_stats(request):
    if request.method == 'POST':
        form = Addstats(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats')
    else:
        form = Addstats ()
    return render(request,'add_stats.html',{'form':form})
    
@login_required(login_url='login')    
def edit_stats(request,pk):
    stats = get_object_or_404(hopitalStats,pk=pk)
    if request.method == 'POST':
        form = EditStats (request.POST, instance=stats)
        if form.is_valid():
            form.save()
            return redirect('stats')
    else:
        form = EditStats(instance=stats)
    return render (request,'edit_stats.html',{'form':form})

@login_required(login_url='login')
def delete_stats(request, pk):
    stats = get_object_or_404(hopitalStats, pk=pk)
    stats.delete()
    return redirect('stats')


#contact US
@login_required(login_url='login')  
def contactUs(request):
    contacts = contact.objects.all().order_by('-id')
    return render(request,'contactUs.html',{'contacts':contacts})