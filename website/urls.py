from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('check-out/', check_out, name='check-out'),
    path('faq/', faq, name='faq'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    

    path('test/', test, name='test'),
]