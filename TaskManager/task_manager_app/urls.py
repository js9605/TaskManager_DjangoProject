from django.urls import path
from .views import task_list, task_detail, task_create, task_edit, task_delete, dashboard

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
    path('tasks/new/', task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
    path('tasks/<int:pk>/update-status/', task_detail, name='update_task_status'),
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'),
    path('dashboard/', dashboard, name='dashboard'),
]