from django.urls import path
from exactdashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

]
