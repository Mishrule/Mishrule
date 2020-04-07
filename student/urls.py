from django.urls import path
from student import views
urlpatterns = [
    path('', views.student, name='student'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('student_manage/', views.student_manage, name='student_manage'),

]
