from django.shortcuts import render
from .models import Post

# Create your views here.


def get_myaande(request):
    posts = Post.objects.all()
    collection = {
        'posts': posts
    }
    return render(request, 'myaande/aande.html', collection)


