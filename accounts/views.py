from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import EmailOrUsernameAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.user.is_authenticated:
        return redirect('website:index')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = EmailOrUsernameAuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = EmailOrUsernameAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('website:index')


def my_account(request):
    return render(request, 'accounts/my-account.html')