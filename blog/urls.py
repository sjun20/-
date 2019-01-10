from django.urls import  include, path
from . import views

urlpatterns = [
    path('', views.parking_list, name='parking_list'),
    path('parking/<int:pk>/', views.parking_detail, name='parking_detail'),
    path('parking/new/', views.parking_new, name='parking_new'),
    path('parking/<int:pk>/edit/', views.parking_edit, name='parking_edit'),
    path('parking/<int:pk>/reserve/', views.add_reserve_to_parking, name='add_reserve_to_parking'),
    path('parking/<int:pk>/<int:pk2>/',views.reserve_detail, name='reserve_detail'),
    path('parking/<int:pk>/<int:pk2>/remove/', views.reserve_remove, name='reserve_remove'),
]
