from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginview, name='login'),
    path('logout/',views.logout,name='logout'),
    

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patient/delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('patient/edit/<int:pk>/', views.edit_patient, name='edit_patient'),
]