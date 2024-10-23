from django.urls import path

from . import views


urlpatterns = [
    path("redirect/", views.user_redirect, name="user_redirect"),
    path('admin/list/', views.AdminListView.as_view(), name='admin_list'),
    path('admin/detail/<int:pk>/', views.AdminDetailView.as_view(), name='admin_detail'),
    path('admin/create/', views.AdminCreateView.as_view(), name='admin_create'),
    path('admin/<int:pk>/update/', views.AdminUpdateView.as_view(), name='admin_update'),
    path('admin/<int:pk>/delete/', views.AdminDeleteView.as_view(), name='admin_delete'),
   # Staff
    path('staff/list/', views.StaffListView.as_view(), name='staff_list'),
    path('staff/create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('staff/detail/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),
    path('staff/update/<int:pk>/', views.StaffUpdateView.as_view(), name='staff_update'),
    path('staff/delete/<int:pk>/', views.StaffDeleteView.as_view(), name='staff_delete'),
    # Librarian
    path('librarian/list/', views.LibrarianListView.as_view(), name='librarian_list'),
    path('librarian/create/', views.LibrarianCreateView.as_view(), name='librarian_create'),
    path('librarian/detail/<int:pk>/', views.LibrarianDetailView.as_view(), name='librarian_detail'),
    path('librarian/update/<int:pk>/', views.LibrarianUpdateView.as_view(), name='librarian_update'),
    path('librarian/delete/<int:pk>/', views.LibrarianDeleteView.as_view(), name='librarian_delete'),
    # Student
    path('student/list/', views.StudentListView.as_view(), name='student_list'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
]
