from django import template
from blog.models import Post, Category


register = template.Library()


@register.inclusion_tag('website/index-recentposts.html')
def index_recentposts():
    posts = Post.objects.filter(status = True).order_by('-published_date')[:3]
    return {'posts': posts}


@register.simple_tag
def check_thumbnail(post):
    if 'default' in post.image_thumbnail.url:
        post.create_thumbnail()
    if post.image_thumbnail is None:
        post.create_thumbnail()
    post.create_thumbnail()
    return 0

@register.inclusion_tag('website/archives-late10posts.html')
def archives_late10posts():
    posts = Post.objects.filter(status = True).order_by('-published_date')[:10]
    return {'posts': posts}


@register.inclusion_tag('website/archives-categories.html')
def archives_by_categories():
    posts = Post.objects.filter(status = True)
    categories = Category.objects.all()
    cat_dict = {}

    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
        
    return {'categories': cat_dict}

