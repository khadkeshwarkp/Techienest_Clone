from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from .forms import CommentsForm
from .models import Post, Comment
# Create your views here.
class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    model = Post
    def get_query_set(self):
    	return self.objects.all()

class BlogPostDetailView(DetailView):
    template_name='blog/blog_post_detail.html'
    form_class=CommentsForm
