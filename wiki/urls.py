from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.categories, name='index'),
    path('<slug:category_slug>', views.items, name='items'),
    path('<slug:category_slug>/<slug:item_slug>', views.item_detail, name='item_detail')
]