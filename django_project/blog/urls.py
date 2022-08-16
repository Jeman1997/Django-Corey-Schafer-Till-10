from django.urls import path
from .views import *
urlpatterns=[
#path('',home,name='blog-home'),
path('',PostListView.as_view(),name='blog-home'),
path('about/',about,name='blog-about'),
path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
path('post/new/',PostCreateView.as_view(),name='post-create'),#searches for 'blog/post_form.list'
path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete')
]
#first path searches for <app>/<model>_<viewtype>.html ie 'blog/post_list.html'
