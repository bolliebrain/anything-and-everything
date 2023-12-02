from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def get_myaande(request):
    posts = Post.objects.all()
    collection = {
        'posts': posts
    }
    return render(request, 'myaande/basehome.html', collection)

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

def edit_myaande(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('seeposts')
    form = PostForm(instance=post)
    collection = {
        'form' : form
    }
    return render(request, 'myaande/edit_post.html', collection)

def delete_myaande(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('seeposts')
