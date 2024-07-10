from django.urls import path
from . import views

app_name = 'bboard'

urlpatterns = [
    path('', views.list_tasks, name='list'),
    path('create/', views.create_task, name='create'),
    path('<int:task_id>/', views.view_task, name='view'),
    path('<int:task_id>/delete/', views.delete_task, name='delete'),
]
