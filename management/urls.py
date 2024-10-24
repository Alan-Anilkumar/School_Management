from django.urls import path
from . import views

urlpatterns = [
    # Grade
    path("grade/", views.GradeListView.as_view(), name="grade_list"),
    path("grade/create/", views.GradeCreateView.as_view(), name="grade_create"),
    path(
        "grade/update/<int:pk>/", views.GradeUpdateView.as_view(), name="grade_update"
    ),
    path(
        "grade/delete/<int:pk>/", views.GradeDeleteView.as_view(), name="grade_delete"
    ),
    # Department
    path("department/", views.DepartmentListView.as_view(), name="department_list"),
    path("department/create/", views.DepartmentCreateView.as_view(), name="department_create"),
    path(
        "department/update/<int:pk>/", views.DepartmentUpdateView.as_view(), name="department_update"
    ),
    path(
        "department/delete/<int:pk>/", views.DepartmentDeleteView.as_view(), name="department_delete"
    ),
    # FeeRecord
    path('fees/', views.FeeRecordListView.as_view(), name='fee_list'),
    path('fees/<int:pk>/', views.FeeRecordDetailView.as_view(), name='fee_detail'),
    path('fees/create/', views.FeeRecordCreateView.as_view(), name='fee_create'),
    path('fees/update/<int:pk>/', views.FeeRecordUpdateView.as_view(), name='fee_update'),
    path('fees/delete/<int:pk>/', views.FeeRecordDeleteView.as_view(), name='fee_delete'),

]
