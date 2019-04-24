from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.utils.http import is_safe_url
from django.contrib import messages

from .models import GuestEmail
from .forms import  LoginForm, RegisterForm, GuestForm
# Create your views here
#

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in")
    #print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post
    if form.is_valid():
        print(form.cleaned_data)
        #context["form"] = LoginForm
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register")

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in")
    #print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post
    if form.is_valid():
        print(form.cleaned_data)
        #context["form"] = LoginForm
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username= username , password= password)
        print(user)

        #print(request.user.is_authenticated)

        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            try:
                del  request.session['guest_email_id']
            except:
                pass
            # Redirect to a success page.
            #context['login_form'] = LoginForm()
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")


        else:
            # Return an 'invalid login' error message.
            print("error")
            #print("hello")
    return render(request, "accounts/login.html" , context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        messages.success(request,'Register Successfully')
    return render(request, "accounts/register.html" ,context)