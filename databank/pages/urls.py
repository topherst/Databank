from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name="notes"),
    path('about/', views.about, name="about"),
    path('cs/', views.cs, name="cs"),
    path('history/', views.history, name="history"),
    path('politics/', views.politics, name="politics"),
    path('philosophy/', views.philosophy, name="philosophy"),
    
]