from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Department, Admin, Staff, Librarian
from .forms import DepartmentForm, AdminForm, StaffForm, LibrarianForm


class AdminDashboard(TemplateView):
    template_name = "admin/admin_dashboard.html"


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "school/department/list.html"
    context_object_name = "departments"
    ordering = ["name"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Departments"
        return context


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "school/department/form.html"
    success_url = reverse_lazy("department-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Department"
        context["button_text"] = "Create"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Department created successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error creating department: {str(e)}")
            return super().form_invalid(form)


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "school/department/form.html"
    success_url = reverse_lazy("department-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Department"
        context["button_text"] = "Update"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Department updated successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error updating department: {str(e)}")
            return super().form_invalid(form)


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = "school/department/confirm_delete.html"
    success_url = reverse_lazy("department-list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Department deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting department: {str(e)}")
            return redirect("department-list")


# Admin Views
class AdminListView(LoginRequiredMixin, ListView):
    model = Admin
    template_name = "school/admin/list.html"
    context_object_name = "admins"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Administrators"
        return context


class AdminCreateView(LoginRequiredMixin, CreateView):
    model = Admin
    form_class = AdminForm
    template_name = "school/admin/form.html"
    success_url = reverse_lazy("admin-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Administrator"
        context["button_text"] = "Create"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Administrator created successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error creating administrator: {str(e)}")
            return super().form_invalid(form)


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Admin
    form_class = AdminForm
    template_name = "school/admin/form.html"
    success_url = reverse_lazy("admin-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Administrator"
        context["button_text"] = "Update"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Administrator updated successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error updating administrator: {str(e)}")
            return super().form_invalid(form)


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    model = Admin
    template_name = "school/admin/confirm_delete.html"
    success_url = reverse_lazy("admin-list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Administrator deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting administrator: {str(e)}")
            return redirect("admin-list")


# Staff Views
class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = "school/staff/list.html"
    context_object_name = "staff"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Staff Members"
        return context


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "school/staff/form.html"
    success_url = reverse_lazy("staff-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Staff Member"
        context["button_text"] = "Create"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Staff member created successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error creating staff member: {str(e)}")
            return super().form_invalid(form)


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = "school/staff/form.html"
    success_url = reverse_lazy("staff-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Staff Member"
        context["button_text"] = "Update"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Staff member updated successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error updating staff member: {str(e)}")
            return super().form_invalid(form)


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = "school/staff/confirm_delete.html"
    success_url = reverse_lazy("staff-list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Staff member deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting staff member: {str(e)}")
            return redirect("staff-list")


# Librarian Views
class LibrarianListView(LoginRequiredMixin, ListView):
    model = Librarian
    template_name = "school/librarian/list.html"
    context_object_name = "librarians"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Librarians"
        return context


class LibrarianCreateView(LoginRequiredMixin, CreateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = "school/librarian/form.html"
    success_url = reverse_lazy("librarian-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Librarian"
        context["button_text"] = "Create"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Librarian created successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error creating librarian: {str(e)}")
            return super().form_invalid(form)


class LibrarianUpdateView(LoginRequiredMixin, UpdateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = "school/librarian/form.html"
    success_url = reverse_lazy("librarian-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Librarian"
        context["button_text"] = "Update"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Librarian updated successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error updating librarian: {str(e)}")
            return super().form_invalid(form)


class LibrarianDeleteView(LoginRequiredMixin, DeleteView):
    model = Librarian
    template_name = "school/librarian/confirm_delete.html"
    success_url = reverse_lazy("librarian-list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Librarian deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting librarian: {str(e)}")
            return redirect("librarian-list")
