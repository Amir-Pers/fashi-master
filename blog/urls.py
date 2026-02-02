from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name='index'),
    path('blog-details/', blog_details, name='blog-details'),
]