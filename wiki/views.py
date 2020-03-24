from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Item


def index(request):
    '''返回主页内容'''
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'wiki/index.html', context)

def item_detail(request, id):
    items = Item.objects.filter(category_id=id)
    # text = items.category_set.all
    context = {'items':items}
    return render(request, 'wiki/item_detail.html', context)