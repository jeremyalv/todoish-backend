from django.urls import path
from todoish import views

urlpatterns = [
    path('', views.Endpoints.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]
