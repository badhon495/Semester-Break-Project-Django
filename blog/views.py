from django.shortcuts import render
# from django.http import HttpResponse #we dont need this as we are now using html directly
from .models import Post


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>') #eta use kora jabe na karon httpsrespons e eto boro html code lekha jhamela. tai amra arekta use kori
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
# Create your views here.


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'}) 