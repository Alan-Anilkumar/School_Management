from django.urls import path
from .import views

urlpatterns = [
    path('records/', views.LibraryRecordListView.as_view(), name='record_list'),
    path('records/create/', views.LibraryRecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', views.LibraryRecordDetailView.as_view(), name='record_detail'),
    path('records/update/<int:pk>/', views.LibraryRecordUpdateView.as_view(), name='record_update'),
    path('records/delete/<int:pk>/', views.LibraryRecordDeleteView.as_view(), name='record_delete'),
]
