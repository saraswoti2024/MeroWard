from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage

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

def events(request):
    return render(request,'myapp/events.html')

def news(request):
    return render(request,'myapp/news.html')

def adminboard(request):
    return render(request,'myapp/adminboard.html')

def dashboard(request):
    return render(request,'myapp/dashboard.html')

def appointments(request):
    return render(request,'myapp/appointments.html')

def complaints(request):
    return render(request,'myapp/complaints.html')


#auth
def log_in(request):
    # return redirect('home')
    return render(request,'auth/log_in.html')

def register(request):
    return render(request,'auth/register.html')