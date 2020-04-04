from django.urls import path
from exact import views

urlpatterns = [
    path('exeat', views.assign_exeat, name='assign_exeat'),
    path('view_exeat', views.view_exeat, name='view_exeat'),
    path('manage_exeat', views.manage_exeat, name='manage_exeat')
]
