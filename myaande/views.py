from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def get_myaande(request):
    posts = Post.objects.all()
    collection = {
        'posts': posts,
    }
    return render(request, 'myaande/basehome.html', collection)

def post_myaande(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('seeposts')
    form = PostForm()
    collection = {
        'form': form,
    }
    return render(request, 'myaande/add_post.html', collection)

def edit_myaande(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.name = request.user
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

def comment_aande(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect ('comment')
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    
    comments = Comment.objects.all()
    
    collection = {
        'comment_form': CommentForm,
        'comments': comments
    }
    return render(request, 'myaande/comment_post.html', collection)