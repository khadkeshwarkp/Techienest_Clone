from django.shortcuts import render

class AboutView(View):
    template_name="company/about.html"

    def get(self,request):
        return render(request,self.template_name)

class CareerView(View):
    template_name="company/career.html"

    def get(self,request):
        return render(request,self.template_name)

class PartnerView(View):
    template_name="company/partner.html"

    def get(self,request):
        return render(request,self.template_name)

class ContactView(View):
    template_name="company/contact.html"

    def get(self,request):
        return render(request,self.template_name)


# Create your views here.
