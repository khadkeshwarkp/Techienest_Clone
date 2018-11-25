from django.contrib import admin
from django.urls import path
from company import views

urlpatterns = [
    re_path(r'^/about/$',views.AboutView.as_view(),name='about'),
    re_path(r'^/career/$',views.CareerView.as_view(),name='career'),
    re_path(r'^/partners/$',views.PartnerView.as_view(),name="partner"),
    re_path(r'^/contact/$',views.ContactView.as_view(),name="contact"),
]
