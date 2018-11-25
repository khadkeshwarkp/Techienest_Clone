from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class BlogList(View):
    template_name = '/.html'
    #form_class=
    def get (self,request):
        return render (request,self.template_name)
class BlogPostDetailView(View):
    template_name=''
    #form_class=
    def get(self,slug,request):
        return render(request,self.template_name)
