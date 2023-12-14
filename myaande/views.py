from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.

class AandeView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'myaande/aande.html'

#def get_myaande(request):
#    posts = Post.objects.all()
#    collection = {
#        'posts': posts,
#    }
#    return render(request, 'myaande/aande.html', collection)

#    class PostAande(View):
#        form_class = PostForm
#        initial = {"key": "value"}
#        template_name = "myaande/add_post.html"

#        def get(self, request, *args, **kwargs):
#            form = self.form_class(initial=self.initial)
#            return render(request, self.template_name, {"form": form})
        
#        def post(self, request, *args, **kwargs):
#            form = self.form_class(request.POST)
#            if form.is_valid():
#                post = form.save(commit=False)
#                post.user = request.user
#                post.save()
#                return redirect('seeposts')
#            return render(request, self.template_name, {"form": form})

class PostAande(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myaande/add_post.html'

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)


#    def post_myaande(request):
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.user = request.user
#            post.save()
#            return redirect('seeposts')
#    form = PostForm()
#    collection = {
#        'form': form,
#    }
#    return render(request, 'myaande/add_post.html', collection)

class EditAande(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "myaande/edit_post.html"



#    def edit_myaande(request, post_id):
#        post = get_object_or_404(Post, id=post_id)
#        if request.method == 'POST':
#            form = PostForm(request.POST, instance=post)
#            if form.is_valid():
#                form.instance.name = request.user
#                form.save()
#                return redirect('seeposts')
#        form = PostForm(instance=post)
#        collection = {
#            'form' : form
#        }
#        return render(request, 'myaande/edit_post.html', collection)

def delete_myaande(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('seeposts')

class CommentView():
    def get(request):
        comments = Comment.objects.get()
        collection = {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm,
                }
        return render(
            request, 'myaande/comment_post.html', collection)
        
    def post(request):
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
            "post": post,
            'comment_form': CommentForm,
            'comments': comments
        }
        return render(request, 'myaande/comment_post.html', collection)