from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Department, Admin, Staff, Librarian
from .forms import DepartmentForm, AdminForm, StaffForm, LibrarianForm


@login_required
def user_redirect(request):
    """Redirects users to their respective dashboards based on user class."""

    if request.user.is_superuser:
        return redirect("admin:index")

    if hasattr(request.user, "doctor"):
        return redirect("doctor_dashboard")
    elif hasattr(request.user, "operator"):
        return redirect("operator_dashboard")
    elif hasattr(request.user, "patient"):
        return redirect("patient_dashboard")
    elif hasattr(request.user, "admin"):
        return redirect("admin_dashboard")
    else:
        raise Http404("You are not registered with the system")


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
    template_name = "admin/admin_list.html"
    context_object_name = "admins"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Administrators"
        return context


class AdminDetailView(DetailView):
    model = Admin
    template_name = "admin/admin_detail.html"
    context_object_name = "admins"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Admin Details"
        return context


class AdminCreateView(LoginRequiredMixin, CreateView):
    model = Admin
    form_class = AdminForm
    template_name = "admin/add_update_admin.html"
    success_url = reverse_lazy("admin_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Administrator"
        context["button_text"] = "Create"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Administrator created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating administrator:")
        return redirect("admin_dashboard")


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Admin
    form_class = AdminForm
    template_name = "admin/add_update_admin.html"
    success_url = reverse_lazy("admin_list")

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
    template_name = "admin/admin_detail.html"
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
    template_name = "staff/staff_list.html"
    context_object_name = "staffs"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Staff Members"
        return context


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staff/staff_detail.html"
    context_object_name = "staffs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Staff Details"
        return context


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "staff/add_update_staff.html"
    success_url = reverse_lazy("staff_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Staff"
        return context

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Staff member created successfully.")
            return response
        except Exception as e:
            messages.error(self.request, f"Error creating staff member: {str(e)}")
            return super().form_invalid(form)

    def form_invalid(self, form):
        print(form.errors, "invalid")
        return redirect("admin_dashboard")


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = "staff/add_update_staff.html"
    success_url = reverse_lazy("staff_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Staff Member"
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
    template_name = "staff/add_update_staff.html"
    success_url = reverse_lazy("staff_list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Staff member deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting staff member: {str(e)}")
            return redirect("staff_list")


# Librarian Views
class LibrarianListView(LoginRequiredMixin, ListView):
    model = Librarian
    template_name = "librarian/librarian_list.html"
    context_object_name = "librarians"
    ordering = ["username"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Librarians"
        return context


class LibrarianDetailView(DetailView):
    model = Librarian
    template_name = "librarian/librarian_detail.html"
    context_object_name = "librarians"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Librarian Details"
        return context


class LibrarianCreateView(LoginRequiredMixin, CreateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = "librarian/add_update_librarian.html"
    success_url = reverse_lazy("librarian_list")

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
    template_name = "librarian/add_update_librarian.html"
    success_url = reverse_lazy("librarian_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Librarian"
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
    template_name = "librarian/add_update_librarian.html"
    success_url = reverse_lazy("librarian_list")

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, "Librarian deleted successfully.")
            return response
        except Exception as e:
            messages.error(request, f"Error deleting librarian: {str(e)}")
            return redirect("librarian-list")
