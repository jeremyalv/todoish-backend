from django.urls import path
from todoish import views

urlpatterns = [
    path('', views.endpoints),
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
]
