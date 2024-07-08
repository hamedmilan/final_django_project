from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/blog-categories.html')
def categories():
    posts = Post.objects.filter(status = True)
    categories = Category.objects.all()
    cat_dict = {}

    mid_index = len(categories) // 2

    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()


    keys1 = categories[:mid_index]
    keys2 = categories[mid_index:]

    dict1 = {key: cat_dict[key] for key in keys1}
    dict2 = {key: cat_dict[key] for key in keys2}

    return {'cat1': dict1, 'cat2': dict2}


@register.inclusion_tag('blog/blog-recentposts.html')
def recentposts(arg=2):
    posts = Post.objects.filter(status = True).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.simple_tag
def check_thumbnail(post):
    if 'default' in post.image_thumbnail.url:
        post.create_thumbnail()
    if post.image_thumbnail is None:
        post.create_thumbnail()
    post.create_thumbnail()
    return 0


