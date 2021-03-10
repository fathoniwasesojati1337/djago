from django.shortcuts import render

def index(request):
    image = {
        'img': '/data/img/anime.jpg'
        }
    return render(request, 'index.html',image)
