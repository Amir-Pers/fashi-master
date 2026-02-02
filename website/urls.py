from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('check-out/', check_out, name='check-out'),
    path('faq/', faq, name='faq'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('product/', product, name='product'),
    path('about-us/', about_us, name='about-us'),
    path('services/', services, name='services'),
    path('my-account/', my_account, name='my-account'),

    path('test/', test, name='test'),
]