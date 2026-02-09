from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def my_account(request):
    return render(request, 'accounts/my-account.html')