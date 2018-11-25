from django.urls import path,re_path
from blog.views import BlogList,BlogPostDetailView
urlpatterns=[
    re_path(r'^$',BlogList.as_view(),name='blog_list'),
    re_path(r'^(?P<slug>\w+)/$',BlogPostDetailView.as_view(),name='blog_post_detail'),
]
