import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from shelf.models import Clipping

from .settings import MEDIA_ROOT, MEDIA_URL


def home(request):
    return render(request, 'home.html')

def userprofile(request, username):
    context = {'username': username}
    return render(request, 'profile.html', context)
    # return HttpResponseRedirect(reverse('home'))

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('document')
        if uploaded_file is not None:
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)
            path_to_file = os.path.join(MEDIA_ROOT, name)
            Clipping.getClippingsFromFile(path_to_file)
        else:
            context['url'] = 'file not selected'
    return render(request, 'upload.html', context)

def random(request):
    number_of_clippings = 5
    random_clippings_list = Clipping.objects.filter(
        kind_of_clipping='Highlight').order_by('?')[:number_of_clippings]
    context = {'random_clippings_list': random_clippings_list}
    return render(request, 'random.html', context=context)
