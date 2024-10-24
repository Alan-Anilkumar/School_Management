from django.urls import path
from .import views

urlpatterns = [
    # library history
    path('records/', views.LibraryRecordListView.as_view(), name='record_list'),
    path('records/create/', views.LibraryRecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', views.LibraryRecordDetailView.as_view(), name='record_detail'),
    path('records/update/<int:pk>/', views.LibraryRecordUpdateView.as_view(), name='record_update'),
    path('records/delete/<int:pk>/', views.LibraryRecordDeleteView.as_view(), name='record_delete'),

    # Book
    path('book/list', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),

]
