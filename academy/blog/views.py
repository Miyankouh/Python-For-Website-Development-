from django.http import HttpResponse
from django.shortcuts import render


def post_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f'post list archive for {year} and {month}')

    if year is not None:
        return HttpResponse(f'post list archive for {year}')

    return HttpResponse('<h2>posts list page</h2></br><h2>posts list page</h2>')


def category_list(request):
    return HttpResponse('category list page')


def post_detail(request, post_title):
    return HttpResponse(f'post detail {post_title}')


def custom_post_detail(request):
    return HttpResponse('custom detail page')
