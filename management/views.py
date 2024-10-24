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

from accounts.decorators import role_required
from .models import Grade, FeeRecord, Department
from .forms import GradeForm, DepartmentForm, FeeRecordForm
from accounts.models import Staff
from django.utils.decorators import method_decorator


@method_decorator(role_required(allowed_roles=["admin", "staff"]), name="dispatch")
class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "management/grade_list.html"
    context_object_name = "grades"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Grade List"
        context["form"] = GradeForm()
        context["staff_list"] = Staff.objects.all()
        return context


@method_decorator(role_required(allowed_roles=["admin", "staff"]), name="dispatch")
class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = "management/add_template.html"
    success_url = reverse_lazy("grade_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Grade"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Grade created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


@method_decorator(role_required(allowed_roles=["admin", "staff"]), name="dispatch")
class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = "management/update_template.html"
    success_url = reverse_lazy("grade_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Grade"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Grade created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("grade_list")


@method_decorator(role_required(allowed_roles=["admin", "staff"]), name="dispatch")
class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    success_url = reverse_lazy("grade_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Grade deleted successfully.")
        return super().delete(request, *args, **kwargs)


@method_decorator(role_required(allowed_roles=["admin"]), name="dispatch")
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "management/department_list.html"
    context_object_name = "departments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Department List"
        context["form"] = DepartmentForm()
        return context


@method_decorator(role_required(allowed_roles=["admin"]), name="dispatch")
class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "management/add_template.html"
    success_url = reverse_lazy("department_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Department"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Department created successfully.")
        return response

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "Error creating record.")
        return redirect("department_list")


@method_decorator(role_required(allowed_roles=["admin"]), name="dispatch")
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "management/update_template.html"
    success_url = reverse_lazy("department_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Department"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Department created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("department_list")


@method_decorator(role_required(allowed_roles=["admin"]), name="dispatch")
class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy("department_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Department deleted successfully.")
        return super().delete(request, *args, **kwargs)


@method_decorator(
    role_required(
        allowed_roles=[
            "admin",
            "staff",
        ]
    ),
    name="dispatch",
)
class FeeRecordListView(LoginRequiredMixin, ListView):
    model = FeeRecord
    template_name = "management/fee_list.html"
    context_object_name = "fee_records"

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get("status")
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Fee List"
        return context


@method_decorator(
    role_required(
        allowed_roles=[
            "admin",
            "staff",
        ]
    ),
    name="dispatch",
)
class FeeRecordDetailView(LoginRequiredMixin, DetailView):
    model = FeeRecord
    template_name = "management/fee_detail.html"
    context_object_name = "fee_record"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Fee Detail"
        fee_record = self.get_object()
        context["student"] = fee_record.student
        return context


@method_decorator(
    role_required(
        allowed_roles=[
            "admin",
            "staff",
        ]
    ),
    name="dispatch",
)
class FeeRecordCreateView(LoginRequiredMixin, CreateView):
    model = FeeRecord
    form_class = FeeRecordForm
    template_name = "management/add_template.html"
    success_url = reverse_lazy("fee_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Fee Record"
        return context


@method_decorator(
    role_required(
        allowed_roles=[
            "admin",
            "staff",
        ]
    ),
    name="dispatch",
)
class FeeRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = FeeRecord
    form_class = FeeRecordForm
    template_name = "management/update_template.html"
    success_url = reverse_lazy("fee_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Fee Record"
        return context


@method_decorator(
    role_required(
        allowed_roles=[
            "admin",
            "staff",
        ]
    ),
    name="dispatch",
)
class FeeRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = FeeRecord
    success_url = reverse_lazy("fee_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)
