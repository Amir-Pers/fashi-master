from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from blog.models import Post, Comment
from django.db.models import Q, F
from django.contrib import messages
from blog.forms import CommentForm

# Create your views here.

def blog(request, **kwargs):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])

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

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submited succesfully')
            return redirect('blog:blog-details', pid=pid)
        else:
            messages.add_message(request, messages.ERROR, 'Your comment didnt submited')
            return redirect('blog:blog-details', pid=pid)
        
    session_key = f'viewed_post_{post.id}'
    if not request.session.get(session_key, False):
        Post.objects.filter(pk=post.pk).update(counted_view=F('counted_view') + 1)
        request.session[session_key] = True
        post.refresh_from_db()

    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()

    context = {
        'post' : post,
        'next_post' : next_post,
        'prev_post' : prev_post,
        'form' : form,
        'comments' : comments,
    }

    return render(request, 'blog/blog-details.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)

    if  (request.method == 'GET'):
        q = request.GET.get('s')
        
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )
        # posts = posts.filter(content__contains=request.GET.get('s'))

    context = {'posts' : posts}

    return render (request, 'blog/blog-home.html', context)