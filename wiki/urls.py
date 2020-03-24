from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>', views.item_list, name='item_list'),
    path('item/<int:id>', views.item_detail, name='item_detail')
]