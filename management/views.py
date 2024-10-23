from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Grade, FeeRecord, Department
from .forms import GradeForm, DepartmentForm
from accounts.models import Staff


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "management/grade_list.html"
    context_object_name = "grades"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = GradeForm()
        context["staff_list"] = Staff.objects.all()
        return context


class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Grade created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Grade created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    success_url = reverse_lazy("grade_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Grade deleted successfully.")
        return super().delete(request, *args, **kwargs)


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "management/department_list.html"
    context_object_name = "grades"


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy("Department_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Department created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy("Department_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Department created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    success_url = reverse_lazy("Department_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Department deleted successfully.")
        return super().delete(request, *args, **kwargs)
