from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from .forms import CommentsForm
# Create your views here.
class BlogList(ListView):
    template_name = 'blog_list.html'

class BlogPostDetailView(DetailView):
    template_name='blog_post_detail.html'
    form_class=CommentsForm
