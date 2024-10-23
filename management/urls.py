from django.urls import path
from . import views

urlpatterns = [
    path("grade/", views.GradeListView.as_view(), name="grade_list"),
    path("grade/create/", views.GradeCreateView.as_view(), name="grade_create"),
    path(
        "grade/update/<int:pk>/", views.GradeUpdateView.as_view(), name="grade_update"
    ),
    path(
        "grade/delete/<int:pk>/", views.GradeDeleteView.as_view(), name="grade_delete"
    ),
]
