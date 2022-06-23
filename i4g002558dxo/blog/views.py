from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy('blog:all')

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy('blog:all')