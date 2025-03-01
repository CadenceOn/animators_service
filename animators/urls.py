from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.request_list, name='request_list'),
    path('register/', views.register, name='register'),
    path('create_request/', views.create_request, name='create_request'),
    path('edit_request/<int:request_id>/', views.edit_request, name='edit_request'),
]