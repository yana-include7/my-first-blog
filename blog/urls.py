from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/windows/', views.post_windows, name='post_windows'),

]

