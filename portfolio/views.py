from django.shortcuts import render


def portfolio_view(request):
    return render(request, 'portfolio/portfolio.html')


def projectimage_view(request):
    return render(request, 'portfolio/project-image.html')

def projectslideshow_view(request):
    return render(request, 'portfolio/project-slideshow.html')
