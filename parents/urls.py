from django.urls import path
from parents import views

urlpatterns = [
    path('parent_info', views.parent_info, name='parent_info')
]
