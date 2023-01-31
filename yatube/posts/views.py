from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница c постами, отфильтрованными по группам.
def group_posts(request):
    return HttpResponse('Групповые посты')


# Страница с полным текстом поста;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Полный текст поста {pk}') 
