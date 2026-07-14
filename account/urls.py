from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginview, name='login'),
    path('logout/',views.logout,name='logout'),
    

    # Dashboards
    path('dashboard/',views.dashboard,name='dashboard')
]