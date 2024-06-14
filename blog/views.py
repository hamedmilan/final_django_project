from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog/blog.html')



def single_view(request):
    return render(request, 'blog/blog-single.html')


