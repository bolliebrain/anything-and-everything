from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.text import slugify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

class AandeView(ListView):
    model = Post
    template_name = 'myaande/aande.html'
    queryset = Post.objects.all()
    
    def get_data(self, **kwargs):
#        posts = super().get_data(**kwargs)
#        posts ['post']= Post.objects.all()
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
            print('Comment saved')

        else:
            comment_form = CommentForm()
        
#        comments = Comment.commentpost

        return render(
            request, 'myaande/post_detail.html',
            {
                "post": post,
                "comment_form": CommentForm(),
                "comments": comments,
            },
        )

#template_name = 'myaande/post_detail.html'
#context_object_name = "post"

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
    success_url = "/"

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        form_class.instance.slug = slugify(form_class.cleaned_data['title'])
        return super().form_valid(form_class)


#    def post_myaande(request):
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.user = request.user
#            post.save()
#            return redirect('seeposts')
#                form = PostForm()
#    collection = {
#        'form': form,
#    }
#    return render(request, 'myaande/add_post.html', collection)

class EditAande(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "myaande/edit_post.html"
    success_url = "/"

class DeleteAande(DeleteView):
    model = Post
    template_name = "myaande/post_confirm_delete.html"
    success_url = "/"

class EditComment(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "myaande/edit_comment.html"

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug':self.object.commentpost.slug})

class DeleteComment(DeleteView):
    model = Comment
    template_name = "myaande/comment_confirm_delete.html"
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug':self.object.commentpost.slug})


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

#def delete_myaande(request, post_id):
#    post = get_object_or_404(Post, id=post_id)
#    post.delete()
#    return redirect('seeposts')

#class CommentView():
#    model = 
#    def get(request):
#        comments = Comment.objects.get()
#        collection = {
#                "post": post,
#                "comments": comments,
#                "comment_form": CommentForm,
#        return render(
#                }
#            request, 'myaande/comment_post.html', collection)
        
#    def post(request):
#        if request.method == 'POST':
#            comment_form = CommentForm(request.POST)
#            if comment_form.is_valid():
#                comment = comment_form.save(commit=False)
#                comment.user = request.user
#                comment.save()
#                return redirect ('comment')
#                comment_form = CommentForm()
#        else:
#            comment_form = CommentForm()

#        comments = Comment.objects.all()
#        collection = {
#            "post": post,
#            'comment_form': CommentForm,
#            'comments': comments
#        }
#        return render(request, 'myaande/comment_post.html', collection)