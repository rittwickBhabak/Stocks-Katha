from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Post

class AllPost(ListView):
    model = Post 
    def get_queryset(self):
        return Post.objects.all().order_by('-edited_at')
    

class ViewPost(DetailView):
    model = Post 

class CreatePost(CreateView):
    fields = "__all__"
    model = Post 

class UpdatePost(UpdateView):
    fields = "__all__"
    model = Post 


