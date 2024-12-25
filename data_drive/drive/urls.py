from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('folder/create/', views.create_folder, name='create_folder'),
    path('folder/<int:id>/', views.view_folder, name='view_folder'),
    path('folder/<int:id>/delete/', views.delete_folder, name='delete_folder'),
    path('file/upload/', views.upload_file, name='upload_file'),
    path('file/<int:id>/delete/', views.delete_file, name='delete_file'),
]
