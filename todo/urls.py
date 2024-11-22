from django.urls import path, include
from .views import index, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, signup, log_in, log_out
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('task-details/<int:pk>/', TaskDetailView.as_view(), name='task-details'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),


    
]