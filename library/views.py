from datetime import date
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from .models import LibraryRecord, Book
from .forms import LibraryRecordForm, BookForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LibrarianDashboard(TemplateView, LoginRequiredMixin):
    template_name = "library/librarian_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Librarian Dashboard"
        return context


class LibraryRecordListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = LibraryRecord
    template_name = "library/record_list.html"
    context_object_name = "records"
    permission_required = "library.view_libraryrecord"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Record List"
        context["form"] = LibraryRecordForm()
        context["edit_forms"] = {
            record.id: LibraryRecordForm(instance=record)
            for record in context["records"]
        }

        return context


class LibraryRecordCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = LibraryRecord
    form_class = LibraryRecordForm
    template_name = "library/add_template.html"
    permission_required = "library.add_libraryrecord"

    success_url = reverse_lazy("record_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Record"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Record created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("record_list")


class LibraryRecordUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = LibraryRecord
    form_class = LibraryRecordForm
    template_name = "library/update_template.html"
    success_url = reverse_lazy("record_list")
    permission_required = "library.change_libraryrecord"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Record"
        # context["grades"] = Grade.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.object:
            kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        return_date = form.cleaned_data.get("return_date")
        due_date = form.cleaned_data.get("due_date")
        if return_date:
            if return_date > due_date:
                form.instance.status = "OVERDUE"
            else:
                form.instance.status = "RETURNED"
        elif due_date and date.today() > due_date:
            form.instance.status = "OVERDUE"
        else:
            form.instance.status = "BORROWED"
        response = super().form_valid(form)
        messages.success(self.request, "Record updated successfully.")
        return response

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "Error updating record.")
        return redirect("record_list")


class LibraryRecordDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = LibraryRecord
    success_url = reverse_lazy("record_list")
    permission_required = "library.delete_libraryrecord"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Record deleted successfully.")
        return response


# View details of a specific library record
class LibraryRecordDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = LibraryRecord
    template_name = "library/record_detail.html"
    context_object_name = "record"


class BookListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    page_title = "Book List"
    permission_required = "accounts.view_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Book List"
        return context


class BookDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"
    page_title = "Book Detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Book Details"
        return context


class BookCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    form_class = BookForm
    template_name = "library/add_template.html"
    success_url = reverse_lazy("book_list")
    permission_required = "library.add_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Book"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Book added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class BookUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    form_class = BookForm
    template_name = "library/update_template.html"
    success_url = reverse_lazy("book_list")
    permission_required = "library.change_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Book"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Book updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class BookDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")
    permission_required = "library.delete_book"

    def form_valid(self, form):
        messages.success(self.request, "Book deleted successfully!")
        return super().form_valid(form)
