from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from blog.models import Post


def post_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f'post list archive for {year} and {month}')

    if year is not None:
        return HttpResponse(f'post list archive for {year}')

    return HttpResponse('<h2>posts list page</h2></br><h2>posts list page</h2>')


class BlogListView(ListView):
    model = Post
    template_name = ".html"


def category_list(request):
    return HttpResponse('category list page')


def post_detail(request, post_title):
    return HttpResponse(f'post detail {post_title}')


class BlogPostDetailView(DetailView):
    model = Post


def custom_post_detail(request):
    return HttpResponse('custom detail page')


def about(request):
    return render(request, 'about.html')


class CustomTemplateView(TemplateView):
    pass
