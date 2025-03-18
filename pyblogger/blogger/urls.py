from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.getPost, name='getPost'),
    path('add-post/', views.addPost, name='add_post'),
]
