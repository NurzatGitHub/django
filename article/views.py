from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy

from .models import*
from .forms import *

menu = [{'title':"О сайте",'url_name' : 'about'},
        {'title':"Добавить сотрудников",'url_name':'add_page'},
        {'title':"Обратная связь",'url_name':'contact'},
        ]

class HomePage(ListView):
     model = User
     template_name = 'article/index.html'
     context_object_name = 'posts'
     extra_context = {'title':'Главная страница'}

     def get_context_data(self,*,object_list = None, **kwargs):
          context =  super().get_context_data(**kwargs)
          context['menu'] = menu
          return context
     
     def get_queryset(self):
          return User.objects.filter(is_published = True)

def about(request):
	return render(request,'article/about.html',{'menu': menu ,'title':'О сайте'})

class AddPage(CreateView):
     form_class = AddPostForm
     template_name = 'article/addpage.html'
     success_url = reverse_lazy('home')

     def get_context_data(self,*,object_list = None, **kwargs):
          context =  super().get_context_data(**kwargs)
          context['title'] = 'Добавление сотрудников'
          context['menu'] = menu
          return context

def contact(request):
     return HttpResponse("Обратная связь")

class ShowPost(DetailView):
     model = User
     template_name = 'article/post.html'
     slug_url_kwarg  ='post_slug'
     context_object_name = 'post'
     def get_context_data(self,*,object_list = None, **kwargs):
          context =  super().get_context_data(**kwargs)
          context['title'] = context['post']
          context['menu'] = menu
          context['salary'] = context['post'].salary
          return context

def PageNotFound(request,exception):
    return HttpResponseNotFound('<h1> СТРАНИЦА НЕ НАЙДЕНА !.</h1>')