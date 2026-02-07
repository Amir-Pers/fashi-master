from django import template
from blog.models import Post, Category
from taggit.models import Tag

register = template.Library()


@register.simple_tag()
def function(a):
    return a + 2 

@register.simple_tag()
def counter():
    count = Post.objects.filter(status=1).count()
    return count

@register.inclusion_tag('blog/blog-recent.html')
def recent_posts(arg=4):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-category.html')
def categories():
    cats = Category.objects.all()
    posts = Post.objects.filter(status=1)
    cat_dict = dict()
    for name in cats:
        if posts.filter(category=name).count() > 0:
            cat_dict[name] = posts.filter(category=name).count()
    return {'categories' : cat_dict}

@register.inclusion_tag('blog/blog-tag.html')
def blog_tags():
    tags =  Tag.objects.all().order_by('-name')
    return {'tags' : tags}