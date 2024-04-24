from django.shortcuts import render,redirect,HttpResponse

from django.http import HttpResponseBadRequest

from django.contrib.auth.models import User

from django.views import View

from trekkings.models import Login

from trekkings.models import Register

from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# from .forms import RegForm
from datetime import datetime
from trekkings.models import Book

from trekkings.models import SlotReservation

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#def login(request):
 #   return  render(request,"login.html")

# def login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
       
        
#         if username =='' or password=='':
#             return render(request,'login.html')
        
#         return render(request,"home.html")
#     else:
#         return render(request,"login.html")

def reg(request):
   return  render(request,"Reg.html")


def home(request):
    return render(request,"home.html")

def packages(request):
    return  render(request,"packages.html")
def travelguide(request):
    return  render(request,"travelguide.html")

# def book(request):
#     return render(request,"book.html")

# def reg(request):
#     return render(request,"Reg.html")

# def reg(request):
#     if request.method=="POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email= request.POST['email']
#         username=request.POST['username']
#         password=request.POST['password']
#         repassword=request.POST['repassword']
#         p=Login.objects.create(username=username,password=password)
#         #p.set_password(password)
#         p.save()
        
#         if first_name=='' or  last_name=='' or email=='' or  username=='' or password=='' or repassword=='':
#             return render(request,"Reg.html")
        
#         u=Register.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password, repassword=repassword)
       
#         u.save()
#         return render(request,"login.html")
    
#     else:
#         return render(request,'Reg.html')

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("login")  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'reg.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('/home/')  # Redirect to the home page
            else:
                # Return an 'invalid login' error message.
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def book(request):
    if request.method == "POST":
        destination = request.POST["destination"]
        duration = request.POST["duration"]
        arrival_date = request.POST["arrival-date"]  # Adjusted field name
        leaving_date = request.POST["leaving-date"]  # Adjusted field name
        details = request.POST["details"]
        
        if destination == '' or duration == '' or arrival_date == '' or leaving_date == '' or details == '':
            return render(request, "home.html")
        
        try:
            b = Book.objects.create(destination=destination, duration=duration, arrival_date=arrival_date,
                                    leaving_date=leaving_date, details=details)
            b.save()
            return render(request, "packages.html")
        except Exception as e:
            # Handle the error, you can print it for debugging purposes
            print("Error:", e)
            return render(request, "error.html")  # Create an error page to display to the user

    else:
        return render(request, "home.html")
    


def bookslot(request):
    if request.method == "POST":
        destination = request.POST.get("destination")
        duration = request.POST.get("duration")
        number_of_members = request.POST.get("number_of_members")
        arrival_date = request.POST.get("arrival-date")  # Adjusted to match your form
        leaving_date = request.POST.get("leaving-date")  # Adjusted to match your form
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        
        # Check if any field is empty
        if not all([destination, duration, arrival_date, leaving_date, name, phone_number, number_of_members]):
            # Consider adding a message about missing information
            return render(request, "bookslot.html")
        
        # Create and save the new SlotReservation instance
        SlotReservation.objects.create(
            destination=destination,
            duration=duration,
            number_of_members=number_of_members,
            arrival_date=arrival_date,
            leaving_date=leaving_date,
            name=name,
            phone_number=phone_number
        )
        
        # Redirecting to the 'packages' page after successful form submission
        return redirect('packages')  # Ensure 'packages' is a valid URL name

    return render(request, "bookslot.html")
