from django.shortcuts import render
from django.views import generic

class AboutView(generic.DetailView):
    template_name="company/about.html"

    def get(self,request):
        return render(request,self.template_name)

class CareerView(generic.DetailView):
    template_name="company/career.html"

    def get(self,request):
        return render(request,self.template_name)

class PartnerView(generic.DetailView):
    template_name="company/partner.html"

    def get(self,request):
        return render(request,self.template_name)

class ContactView(generic.DetailView):
    template_name="company/contact.html"

    def get(self,request):
        return render(request,self.template_name)


# Create your views here.
