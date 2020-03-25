from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Item


def categories(request):
    '''返回主页内容'''
    categories = Category.objects.order_by('created_at')
    context = {'categories': categories}
    return render(request, 'wiki/categories.html', context)

def items(request, id):
    category = Category.objects.get(id=id)
    items = category.item_set.order_by('-created_at')
    # text = items.category_set.all
    context = {'category': category, 'items': items}
    return render(request, 'wiki/items.html', context)

def item_detail(request,category_id, item_id):
    category = Category.objects.get(id=category_id)
    items = category.item_set.get(id=item_id)

    context = {'item_name':items.item_name, 'item_text':items.item_body}

    return render(request, 'wiki/item_detail.html', context)
