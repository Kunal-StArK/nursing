from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home'),
    path('services/',views.servicesview, name='services'),
    path('departments/',views.departmentsview, name='departments'),
    path('contact/',views.contactview,name='contacts'),
    path('gallery/',views.galleryview,name='gallery'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]