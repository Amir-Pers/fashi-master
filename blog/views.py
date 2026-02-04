from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post, Category 

# Create your views here.

def blog(request, **kwargs):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    context = {
        'posts' : posts
    }

    return render(request, 'blog/blog-home.html', context)


def blog_details(request, **kwargs):
    pid = kwargs.get('pid')
    posts = Post.objects.filter(status=1)
    if not pid:
        raise Http404('Post Not Found')

    post = get_object_or_404(posts, pk=pid)
    next_post = posts.filter(published_date__gt=post.published_date).order_by('published_date').first()
    prev_post = posts.filter(published_date__lt=post.published_date).order_by('-published_date').first()

    context = {
        'post' : post,
        'next_post' : next_post,
        'prev_post' : prev_post,
    }
    return render(request, 'blog/blog-details.html', context)

