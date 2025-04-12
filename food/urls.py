# from django.contrib import admin
from django.urls import path
from . import views


#Namespacing
app_name = 'food'
urlpatterns = [
    #/food/
    # path('', views.index, name='index'),
    path('', views.IndexClassView.as_view(),name='index'),

    path('item/', views.item, name='item'),

    #/food/item_id
    # path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    
    #add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    
    #edit item
    path('update/<int:id>/',views.update_item,name='update_item'),

    #delete item
    # path('delete/<int:id>/',views.delete_item,name='delete_item'),
    path('delete/<int:pk>/',views.DeleteItem.as_view(),name='DeleteItem'),


]
