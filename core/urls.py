from django.urls import path
from . import views
urlpatterns = [

    path('',views.Home,name='Home'),
    path('list_all/',views.list_all,name='list_all'),
    path('list_one/<pk>',views.list_one,name='list_one'),
    path('search/',views.search,name='search'),

]