from django.urls import path

from . import views


urlpatterns = [
    path('staff/dashboard/', views.StaffDashboard.as_view(), name='staff_dashboard'),
   
]
