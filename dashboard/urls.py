from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('lost/', views.lost, name='dashboard-lost'),
    path('found/', views.found, name='dashboard-found'),
    path('solve/<int:pk>', views.laporan_solve, name='dashboard-laporan-solve'),
    path('solved/', views.solved, name='dashboard-solved'),

]
