from django.urls import path
from . import views

urlpatterns = [
        path('register/', views.register, name='register'),
        path('getExhibition/', views.getExhibition, name='getExhibition'),
        path('delete/', views.deleteExhibition, name='deleteExhibition'),
        path('getData/', views.getData, name='getData'),
        path('upload/', views.upload, name='upload'),
        path('create/', views.create, name='create'),
        path('joinInfo/', views.joinInfo, name='create'),
]
