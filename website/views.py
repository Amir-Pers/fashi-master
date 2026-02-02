from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def shop(request):
    return render(request, 'website/shop.html')

def contact(request):
    return render(request, 'website/contact.html')

def shopping_cart(request):
    return render(request, 'website/shopping-cart.html')

def check_out(request):
    return render(request, 'website/check-out.html')

def faq(request):
    return render(request, 'website/faq.html')

def register(request):
    return render(request, 'website/register.html')

def login(request):
    return render(request, 'website/login.html')

def product(request):
    return render(request, 'website/product.html')



def test(request):
    return HttpResponse('<h1>salam</h1>')

