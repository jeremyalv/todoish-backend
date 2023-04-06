from django.urls import path
from todoish import views

urlpatterns = [
    path('', views.endpoints)
]
