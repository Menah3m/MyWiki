from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.item_detail, name='item_detail'),
]