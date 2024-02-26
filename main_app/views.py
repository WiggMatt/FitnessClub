from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main_app.forms import RegistrationForm, LoginForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, authenticate_user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'main_app/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('#')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, 'main_app/login.html', {'form': form})


def main_view(request):
    return render(request, 'main_app/main.html')


def abonement_view(request):
    return render(request, 'main_app/abonements.html')
