from django.urls import path
from . import  views


urlpatterns = [
    path('', views.apiView, name='api-overview'),
    path('task-list/', views.tasklist, name='api-list'),
    path('task-detail/<str:pk>/', views.taskdetail, name='api-details'),
    path('task-create/', views.taskcreate, name='api-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='api-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='api-delete'),
]

