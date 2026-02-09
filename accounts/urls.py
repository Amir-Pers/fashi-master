from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('my-account/', my_account, name='my-account'),
]