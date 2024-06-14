from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')


def archives_view(request):
    return render(request, 'website/archives.html')

