from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('features/', views.features_view, name='features_page'),
]