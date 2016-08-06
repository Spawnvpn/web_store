from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import LoginForm, RegisterUserForm


def login_user(request):
    if request.user.is_authenticated():
        return redirect('/')
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return redirect(reverse('login'))


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterUserForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.save()
        user.set_password(form.cleaned_data.get('password1'))
        user.save()
        return redirect('/')
    return render(request, 'users/register.html', context={'form': form,
                                                           'name': 'Register'})
