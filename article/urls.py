from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('about/',about,name='about'),
    path('addpage/',AddPage.as_view(),name='add_page'),
    path('contact/',contact,name='contact'),
    path('post/<str:post_slug>/',ShowPost.as_view(),name='post'),
]