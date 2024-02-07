from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"DEBUG: User created - {user.username}, {user.email}")

            login(request, user)
            if request.user.is_authenticated:
                print("DEBUG: User authenticated")
            else:
                print("DEBUG: User NOT authenticated")

            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("home")

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("DEBUG: User is not None")
                print("DEBUG: User authenticated:", user)
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")

                return redirect("home")
            else:
                print(f"DEBUG: User is None")
                messages.error(request, "Invalid username or password.")
                print("DEBUG: Authentication failed. Error message:", form.errors.get('__all__'))
        else:
            print("DEBUG: Form is invalid")
            print("DEBUG: Form errors:", form.errors)
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
