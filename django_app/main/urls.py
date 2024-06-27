from django.urls import path

from . import views

urlpatterns = [
    path('create_video/', views.create_video_view, name='create_video'),
]
