from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.Endpoints.as_view()),
    path('users/', views.ProfileList.as_view()),
    path('users/<int:pk>/', views.ProfileDetail.as_view()),
]