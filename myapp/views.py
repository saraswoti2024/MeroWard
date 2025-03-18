from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def services(request):
    return render(request,'myapp/services.html')

def contacts(request):
    return render(request,'myapp/contacts.html')

def events(request):
    return render(request,'myapp/events.html')

def news(request):
    return render(request,'myapp/news.html')

def adminboard(request):
    return render(request,'myapp/adminboard.html')

def dashboard(request):
    return render(request,'myapp/dashboard.html')

#auth
def log_in(request):
    return redirect('home')
    # return render(request,'auth/log_in.html')

def register(request):
    return redirect('log_in')