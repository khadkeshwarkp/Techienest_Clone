from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
     path('',views.ProductList.as_view(),name="product_list"),
     re_path(r'^(?P<slug>\w+)/$',views.ProductDetail.as_view(),name="product_detail"),
]
