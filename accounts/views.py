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
from .models import Admin, Staff, Librarian, Student
from .forms import AdminForm, StaffForm, LibrarianForm, StudentForm


@login_required
def user_redirect(request):
    """Redirects users to their respective dashboards based on user class."""

    if hasattr(request.user, "admin"):
        return redirect("admin_dashboard")
    elif hasattr(request.user, "staff"):
        return redirect("staff_dashboard")
    elif hasattr(request.user, "librarian"):
        return redirect("librarian_dashboard")
    else:
        raise Http404("You are not registered with the system")


# class DepartmentListView(LoginRequiredMixin, ListView):
#     model = Department
#     template_name = "school/department/list.html"
#     context_object_name = "departments"
#     ordering = ["name"]
#

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page_title"] = "Departments"
#         return context


# class DepartmentCreateView(LoginRequiredMixin, CreateView):
#     model = Department
#     form_class = DepartmentForm
#     template_name = "school/department/form.html"
#     success_url = reverse_lazy("department-list")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page_title"] = "Create Department"
#         context["button_text"] = "Create"
#         return context

#     def form_valid(self, form):
#         try:
#             response = super().form_valid(form)
#             messages.success(self.request, "Department created successfully.")
#             return response
#         except Exception as e:
#             messages.error(self.request, f"Error creating department: {str(e)}")
#             return super().form_invalid(form)


# class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
#     model = Department
#     form_class = DepartmentForm
#     template_name = "school/department/form.html"
#     success_url = reverse_lazy("department-list")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page_title"] = "Update Department"
#         context["button_text"] = "Update"
#         return context

#     def form_valid(self, form):
#         try:
#             response = super().form_valid(form)
#             messages.success(self.request, "Department updated successfully.")
#             return response
#         except Exception as e:
#             messages.error(self.request, f"Error updating department: {str(e)}")
#             return super().form_invalid(form)


# class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Department
#     template_name = "school/department/confirm_delete.html"
#     success_url = reverse_lazy("department-list")

#     def delete(self, request, *args, **kwargs):
#         try:
#             response = super().delete(request, *args, **kwargs)
#             messages.success(request, "Department deleted successfully.")
#             return response
#         except Exception as e:
#             messages.error(request, f"Error deleting department: {str(e)}")
#             return redirect("department-list")


# Admin Views
class AdminListView(LoginRequiredMixin, ListView):
    model = Admin
    template_name = "accounts/admin_list.html"
    context_object_name = "admins"
    ordering = ["username"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Administrators"
        return context


class AdminDetailView(LoginRequiredMixin, DetailView):
    model = Admin
    template_name = "accounts/admin_detail.html"
    context_object_name = "admins"
    user = Admin.objects.get(username='Admin')
    print(user.profile_picture)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Admin Details"
        return context


class AdminCreateView(LoginRequiredMixin, CreateView):
    model = Admin
    form_class = AdminForm
    template_name = "accounts/add_update_admin.html"
    success_url = reverse_lazy("admin_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Administrator"

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Administrator created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating administrator:")
        return redirect("admin_list")


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Admin
    form_class = AdminForm
    template_name = "accounts/add_update_admin.html"
    success_url = reverse_lazy("admin_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Administrator"
        context["button_text"] = "Update"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Administrator updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating administrator:")
        return redirect("admin_list")


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    model = Admin
    success_url = reverse_lazy("admin_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)


# Staff Views
class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = "accounts/staff_list.html"
    context_object_name = "staffs"
    ordering = ["username"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Staff Members"
        return context


class StaffDetailView(DetailView):
    model = Staff
    template_name = "accounts/staff_detail.html"
    context_object_name = "staffs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Staff Details"
        return context


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "accounts/add_update_staff.html"
    success_url = reverse_lazy("staff_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Staff"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Staff member created successfully.")
        return response

    def form_invalid(self, form):
        messages.success(self.request, "An error occurred creating failed.")
        return redirect("staff_list")


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = "accounts/add_update_staff.html"
    success_url = reverse_lazy("staff_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Staff Member"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Staff member updated successfully.")
        return response

    def form_invalid(self, form):
        messages.success(self.request, "An error occurred updating failed.")
        return redirect("staff_list")


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy("staff_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)


# Librarian Views
class LibrarianListView(LoginRequiredMixin, ListView):
    model = Librarian
    template_name = "accounts/librarian_list.html"
    context_object_name = "librarians"
    ordering = ["username"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Librarians"
        return context


class LibrarianDetailView(DetailView):
    model = Librarian
    template_name = "accounts/librarian_detail.html"
    context_object_name = "librarians"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Librarian Details"
        return context


class LibrarianCreateView(LoginRequiredMixin, CreateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = "accounts/add_update_librarian.html"
    success_url = reverse_lazy("librarian_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Librarian"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Librarian created successfully.")
        return response

    def form_invalid(self, form):
        messages.success(self.request, "An error occurred creating failed.")
        return redirect("librarian_list")


class LibrarianUpdateView(LoginRequiredMixin, UpdateView):
    model = Librarian
    form_class = LibrarianForm
    template_name = "accounts/add_update_librarian.html"
    success_url = reverse_lazy("librarian_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Librarian"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Librarian updated successfully.")
        return response

    def form_invalid(self, form):
        messages.success(self.request, "An error occurred updating failed.")
        return redirect("librarian_list")


class LibrarianDeleteView(LoginRequiredMixin, DeleteView):
    model = Librarian
    success_url = reverse_lazy("librarian_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "accounts/student_list.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Student List"
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "accounts/student_detail.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Student List"
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = "accounts/add_update_student.html"
    form_class = StudentForm
    success_url = reverse_lazy("student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create STudent"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student  created successfully.")
        return response

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "An error occurred while creating the form.")
        return self.render_to_response(self.get_context_data(form=form))


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = "accounts/add_update_student.html"
    form_class = StudentForm
    success_url = reverse_lazy("student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update STudent"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student  updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "An error occurred while creating the form.")
        return self.render_to_response(self.get_context_data(form=form))


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Librarian deleted successfully.")
        return super().delete(request, *args, **kwargs)
