from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post

class PostDetailView(DetailView):    
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    model = Post