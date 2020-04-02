from django.urls import path
from staff import views

urlpatterns = [
    path('staff_registration', views.staff_Registration, name='staff_registration'),
    path('staff_profile', views.staff_Profile, name='staff_profile'),
    path('staff_management', views.staff_Management, name='staff_management')
]
