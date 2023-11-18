from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def get_myaande(request):
    posts = Post.objects.all()
    collection = {
        'posts': posts
    }
    return render(request, 'myaande/aande.html', collection)

def post_myaande(request):
    if request.method == 'POST':
        title = request.POST.get('title_name')
        description = request.POST.get('description_name')
        dateposted = request.POST.get('date_name')
        Post.objects.create(title=title, description=description, dateposted=dateposted)

        return redirect('seeposts')
    return render(request, 'myaande/add_post.html')


