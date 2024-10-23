from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Grade, FeeRecord, Department
from .forms import GradeForm


class GradeListView(ListView):
    model = Grade
    template_name = "management/grade_list.html"
    context_object_name = "grades"


class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Record created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("record_list")


class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Record created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("record_list")


class GradeDeleteView(DeleteView):
    model = Grade
    success_url = reverse_lazy("grade_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)
