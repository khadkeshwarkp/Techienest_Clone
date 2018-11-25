from django.contrib import admin
from django.urls import path,re_path

urlpatterns=[
     path('',views.ProductList.as_view(),name="product_list"),
     re_path(r'^/(?P<slug>\w+)/$',ProductDetail.as_view(),name="product_detail"),
]
