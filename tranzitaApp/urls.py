from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('urlConvert/', views.urlConvert, name="urlConvert"),
    path('deleteURL/<int:id>/', views.deleteURL, name="deleteURL"),
]