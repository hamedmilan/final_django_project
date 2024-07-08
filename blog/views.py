from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, **kwargs):

    posts = Post.objects.filter(status=True)
    
    if 'author_username' in kwargs:
        posts = posts.filter(author__username = kwargs['author_username']) 

    if 'cat_name' in kwargs:
        posts = posts.filter(category__name = kwargs['cat_name'])
                                    
    

    posts = posts.filter(published_date__lte=timezone.now()).order_by('-published_date')

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)

    context = {'posts':posts}
    return render(request, 'blog/blog.html', context)



def single_view(request, pid):

    posts = Post.objects.filter(status = True, published_date__lte=timezone.now()).order_by('published_date')
    
    the_post = get_object_or_404(posts, id=pid)
    the_post.counted_view += 1
    the_post.save()
    context = {'post':the_post}

    return render(request, 'blog/blog-single.html', context)


