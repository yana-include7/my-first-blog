from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Photo
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import logging
logger = logging.getLogger("mylogger")

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_view.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_edit.html', {'posts': posts})

def post_windows(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/windows.html', {'post': post})

def post_remove(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_message.html', {'post': post})

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'


class PhotoUpdate(UpdateView):
    model =  Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model =  Photo

