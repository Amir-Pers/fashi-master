from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name='index'),
    path('blog-details/', blog_details, name='blog-details'),
    path('blog-details/<int:pid>/', blog_details, name='blog-details'),
    path('category/<str:cat_name>/', blog, name='category'),
    path('tag/<str:tag_name>/', blog, name='tag'),
    path('author/<str:author_username>/', blog, name='author'),
    path('search/', blog_search, name='search'),

]