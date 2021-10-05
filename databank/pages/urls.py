from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.NotePostList.as_view(), name="notes"),
    path('<slug:slug>/', views.NotePostDetail.as_view(), name="notepost_detail"),
    path('about/', views.about, name="about"),  
]