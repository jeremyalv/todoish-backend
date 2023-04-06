from django.urls import path
from authentication import views


urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('logout/', views.logout)
]