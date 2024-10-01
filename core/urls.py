from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insertData, name = 'insert')
]