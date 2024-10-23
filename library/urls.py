from django.urls import path
from .views import LibraryRecordListView, LibraryRecordCreateView, LibraryRecordUpdateView, LibraryRecordDeleteView, LibraryRecordDetailView

urlpatterns = [
    path('records/', LibraryRecordListView.as_view(), name='library_record_list'),
    path('records/create/', LibraryRecordCreateView.as_view(), name='library_record_create'),
    path('records/<int:pk>/', LibraryRecordDetailView.as_view(), name='library_record_detail'),
    path('records/update/<int:pk>/', LibraryRecordUpdateView.as_view(), name='library_record_update'),
    path('records/delete/<int:pk>/', LibraryRecordDeleteView.as_view(), name='library_record_delete'),
]
