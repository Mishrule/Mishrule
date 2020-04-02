from django.urls import path
from exactdashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('student/', views.student, name='student'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('student_manage/', views.student_manage, name='student_manage'),

]
