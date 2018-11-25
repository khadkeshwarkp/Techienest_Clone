from django.shortcuts import render
from django.views.generic import View,DetailView,CreateView,DeleteView,ListView
from .models import Products


class ProductList(ListView):
    model=Products
    template_name="services/productlist.html"

class ProductDetail(DetailView):
    model=Products
    template_name="services/productdetail.html"
# Create your views here.
