from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("DEBUG here")
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print("DEBUG: Form errors:", form.errors)
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("home")
