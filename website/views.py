from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages



def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket has been submitted successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket has not been submitted successfully!')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def archives_view(request):
    return render(request, 'website/archives.html')

