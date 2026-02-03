from django.shortcuts import render
from blog.models import Post, Category 

# Create your views here.

def blog(request):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    context = {
        'posts' : posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_details(request):
    return render(request, 'blog/blog-details.html')

