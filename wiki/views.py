from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Item


def index(request):
    '''返回主页内容'''
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'wiki/index.html', context)