from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.text import slugify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

class AandeView(ListView):
    model = Post
    template_name = 'myaande/aande.html'
    queryset = Post.objects.all()
    paginate_by = 6

    def get_data(self, **kwargs):
        return queryset

class AandeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(commentpost=post.pk)
        print(f'comments {comments}')

        return render(
            request, 
            'myaande/post_detail.html',
            {
                "post": post,
                "comment_form": CommentForm(),
                "comments": comments,
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        model = Comment
        form_class = CommentForm

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(commentpost=post.pk)

        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = self.request.user
            comment.commentpost = post
            comment.save()
            messages.success(self.request, 'Commented Successfully' )

        else:
            comment_form = CommentForm()

        return render(
            request, 'myaande/post_detail.html',
            {
                "post": post,
                "comment_form": CommentForm(),
                "comments": comments,
            },
        )

class PostAande(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myaande/add_post.html'
    success_url = "/"
#    success_message = "Posted Successfully"

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        form_class.instance.slug = slugify(form_class.cleaned_data['title'])
        return super().form_valid(form_class)
    
    def get_success_url(self):
        messages.success(self.request, 'Posted Successfully' )
        return reverse_lazy('post_detail', kwargs={'slug':self.object.slug})

class EditAande(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "myaande/edit_post.html"
#   success_message = "Post Updated Successfully"
    
    def get_success_url(self):
        messages.success(self.request, 'Post Updated Successfully' )
        return reverse_lazy('post_detail', kwargs={'slug':self.object.slug})

class DeleteAande(DeleteView):
    model = Post
    template_name = "myaande/post_confirm_delete.html"
    success_url = "/"

    def get_success_url(self):
        return reverse_lazy('allmyposts', kwargs={'slug':self.object.slug})

class EditComment(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "myaande/edit_comment.html"
#    success_message = "Updated Comment Successfully"

    def get_success_url(self):
        messages.success(self.request, 'Updated Comment Successfully' )
        return reverse_lazy('post_detail', kwargs={'slug':self.object.commentpost.slug})

class DeleteComment(DeleteView):
    model = Comment
    template_name = "myaande/comment_confirm_delete.html"
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug':self.object.commentpost.slug})

class AllMyPosts(View):
    model = Post
    template_name = "myaande/allmyposts.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(user=request.user)
        print(queryset)
        
        return render(
            request, 
            'myaande/allmyposts.html',
            {
                 "posts": queryset,
            },
        )