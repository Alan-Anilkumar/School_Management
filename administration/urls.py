from django.urls import path

from . import views


urlpatterns = [
    path('dashboard/', views.AdminDashboard.as_view(), name='admin_dashboard'),
]
