from django.shortcuts import render
from .models import Category, Post
from django.http import Http404
# Create your views here.
def index(request):
    posts=Post.objects.all()

    return render (request, 'index.html', {'posts':posts})
def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post.html', {'post': post})