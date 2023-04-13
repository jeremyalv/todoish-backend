from django.urls import path, include

from todoish import views as todoish_views
from authentication import views as auth_views

urlpatterns = [
    # Todoish
    path('', todoish_views.APIRoot.as_view()),
    path('api', todoish_views.Endpoints.as_view()),
    path('tasks/', todoish_views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', todoish_views.TaskDetail.as_view(), name='task-detail'),

    # Auth
    path('auth/', auth_views.Endpoints.as_view()),
    path('auth/users/', auth_views.ProfileList.as_view(), name='user-list'),
    path('auth/users/<int:pk>/', auth_views.ProfileDetail.as_view(), name='user-detail'),
]
