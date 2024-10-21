from django.urls import path

from . import views


urlpatterns = [
# # Admin
#     path('admin/list/', views.AdminListView.as_view(), name='admin-list'),
#     path('admin/create/', views.AdminCreateView.as_view(), name='admin-create'),
#     path('admin/<int:pk>/update/', views.AdminUpdateView.as_view(), name='admin-update'),
#     path('admin/<int:pk>/delete/', views.AdminDeleteView.as_view(), name='admin-delete'),

#     # Staff
#     path('staff/list/', views.StaffListView.as_view(), name='staff-list'),
#     path('staff/create/', views.StaffCreateView.as_view(), name='staff-create'),
#     path('staff/<int:pk>/update/', views.StaffUpdateView.as_view(), name='staff-update'),
#     path('staff/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff-delete'),

#     # Librarian
#     path('librarian/list/', views.LibrarianListView.as_view(), name='librarian-list'),
#     path('librarian/create/', views.LibrarianCreateView.as_view(), name='librarian-create'),
#     path('librarian/<int:pk>/update/', views.LibrarianUpdateView.as_view(), name='librarian-update'),
#     path('librarian/<int:pk>/delete/', views.LibrarianDeleteView.as_view(), name='librarian-delete'),
]
