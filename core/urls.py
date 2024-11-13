from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insertData, name = 'insert'),
    path('viewdata/', views.viewData, name = 'viewdata'),
    path('updatedata/<id>/', views.updateData, name = 'updatedata'),
    path('deletedata/<id>/', views.deleteData, name = 'deletedata'),

    #API
    path('api/', views.ApiListViewCreate.as_view(), name='apiview'),
    path('api/<int:pk>/', views.ApiRetrieveUpdateDestroy.as_view(), name = 'retrieveupdatedestroy')
]