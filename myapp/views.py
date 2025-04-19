from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from datetime import datetime,timedelta
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
# from django.contrib.auth.models import CustomUserModel
from .models import CustomUserModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import re

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def services(request):
    return render(request,'myapp/services.html')

def contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] 
            try:
                detail = Contact(name=name,email=email,message=message)
                detail.full_clean()
                detail.save()
                  ###### send mail #########
                subject = "Thank you for getting in Touch!"
                message = render_to_string('myapp/gmail.html',{'name':name,'date':datetime.now()})
                from_email = 'saraswotikhadka2k2@gmail.com'
                recipient_list = [email] 
                emailmsg = EmailMessage(subject,message,from_email,recipient_list)
                emailmsg.send(fail_silently=True)
                messages.success(request,'successfully sent!')
                return redirect('contacts')
            except Exception as e:
                messages.error(request,f'{str(e)}')
                return redirect('contacts')
    return render(request,'myapp/contacts.html',{'form':form})

def complete(request,id):
    data = AppointmentForm.objects.get(id=id)
    data.iscomplete=True
    data.isschedule=False
    data.save()
    next_page = request.GET.get('next')
    if next_page == 'scheduled':
        return redirect('scheduled')
    else:
        return redirect('adminboard')

def completed(request):
    data = AppointmentForm.objects.filter(iscomplete=True)
    context={
        'data':data,
    }
    return render(request,'myapp/completed.html',context)


def adminboard(request):
    total_appointment = AppointmentForm.objects.count()
    appointment = AppointmentForm.objects.filter(iscomplete=False)
    total_users = CustomUserModel.objects.count()
    total_contact = Contact.objects.count()
    context={
        'totala':total_appointment,
        'totalu':total_users,
        'totalc':total_contact,
        'appointment':appointment,
    }
    return render(request,'myapp/adminboard.html',context)


@login_required(login_url='log_in')
def appointments(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        wardno = request.POST['ward']
        request_type = request.POST.get('emergency')=='on'
        certificate = request.POST.getlist('certificate')
        try:
            AppointmentForm.objects.create(fullname=fullname,email=email,ward=wardno,request_type=request_type,certificates=certificate)
            messages.success(request,'sent successfully!')
            return redirect('appointments')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('appointments')
    return render(request,'myapp/appointments.html')


@login_required(login_url='log_in')
def view_app(request):
    return render(request,'myapp/view_app.html')

#auth
def log_in(request):
    if request.method=='POST':
        uname = request.POST['username']
        password = request.POST['password']
        if not CustomUserModel.objects.filter(username=uname).exists():
            messages.error(request,'username doesnot exists!')
            return redirect('log_in')
        people = authenticate(username=uname,password=password)
        if people is not None:
            login(request,people)
            next1 = request.POST.get('next','')
            if next1 and next1 != 'None' and next1 != '':  
                return redirect(next1)  # Redirect to the 'next' URL if it's valid
            else:
                return redirect('home')
        else:
            messages.error(request,'invalid password!')
            return redirect('log_in')
    next = request.GET.get('next')
    return render(request,'auth/log_in.html',{'next':next})

def register(request):
    if request.method=='POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            try:
                validate_password(password) 
                if password== uname:
                    messages.error(request,'password and uname shouldn\'t be same')
                if not re.search(r'[A-Z]',password):
                    messages.error(request,'password should contain at least one upper letter')
                    return redirect('register')
                if not re.search(r'\d',password):
                    messages.error(request,'password should at least contain one number')
                    return redirect('register')
                if not re.search(r'\W',password):
                    messages.error(request,'password should at least contain one special character')
                    return redirect('register')
                if CustomUserModel.objects.filter(username=uname).exists():
                    messages.error(request,'username already exists!')
                    return redirect('register')
                if CustomUserModel.objects.filter(email=email).exists():
                    messages.error(request,'email already exists!')
                    return redirect('register')
                CustomUserModel.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password,word_no=13)
                messages.success(request,'Register successfully!<br>Redirecting to login page......')
                return redirect('register')
            except Exception as e:
                messages.error(request,f'{str(e)}')
                return redirect('register')
        else:
            messages.error(request,'password and confirm password should match!!')
            return redirect('register')
    return render(request,'auth/register.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

def profile_dashboard(request):
    return render(request,'profile/profile_dashboard.html')

@login_required(login_url='log_in')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'auth/change_password.html',{'form':form})

def settings(request):
    return render(request,'auth/settings.html')

def schedule(request,id):
            data = AppointmentForm.objects.get(id=id)
            emails = data.email[0:5]
            subject = "welcome Message"
            message = render_to_string('myapp/gmail2.html',{'emails':emails,'date':(datetime.now()+timedelta(days=1)).date()})
            from_email = 'saraswotikhadka2k2@gmail.com'
            recipient_list = [data.email] ##current database store submit
        # send_mail(subject,message,from_email,recipient_list)
            emailmsg = EmailMessage(subject,message,from_email,recipient_list)
            emailmsg.send(fail_silently=True)
            data.isschedule = True
            data.save()
            return redirect('adminboard')

def scheduled(request):
    data = AppointmentForm.objects.filter(isschedule=True)
    return render(request,'myapp/scheduled.html',{'data':data})