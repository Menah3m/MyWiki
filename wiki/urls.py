from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.categories, name='index'),
    path('<int:id>', views.items, name='items'),
    path('<int:category_id>/<int:item_id>', views.item_detail, name='item_detail')
]