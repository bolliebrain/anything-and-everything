from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def get_myaande(request):
    posts = Post.objects.all()
    collection = {
        'posts': posts
    }
    return render(request, 'myaande/aande.html', collection)

def post_myaande(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seeposts')
    form = PostForm()
    collection = {
        'form' : form
    }
    return render(request, 'myaande/add_post.html', collection)


