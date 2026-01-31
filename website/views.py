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



def test(request):
    return HttpResponse('<h1>salam</h1>')


''' 

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('shopping-cart', shopping_cart, name='shopping-cart'),
    path('check-out', check_out, name='check-out'),
    path('faq', faq, name='faq'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    
]
'''