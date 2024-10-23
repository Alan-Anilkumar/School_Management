from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import LibraryRecord, Book
from .forms import LibraryRecordForm, BookForm
from django.contrib import messages


class LibraryRecordListView(ListView):
    model = LibraryRecord
    template_name = "library/record_list.html"
    context_object_name = "records"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = LibraryRecordForm()
        context["edit_forms"] = {
            record.id: LibraryRecordForm(instance=record)
            for record in context["records"]
        }

        return context


class LibraryRecordCreateView(CreateView):
    model = LibraryRecord
    form_class = LibraryRecordForm
    success_url = reverse_lazy("record_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Record created successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error creating record.")
        return redirect("record_list")


class LibraryRecordUpdateView(UpdateView):
    model = LibraryRecord
    form_class = LibraryRecordForm
    success_url = reverse_lazy("record_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.object:
            kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Record updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error updating record.")
        return self.render_to_response(self.get_context_data(form=form))


class LibraryRecordDeleteView(DeleteView):
    model = LibraryRecord
    success_url = reverse_lazy("record_list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Record deleted successfully.")
        return response


# View details of a specific library record
class LibraryRecordDetailView(DetailView):
    model = LibraryRecord
    template_name = "library/record_detail.html"
    context_object_name = "record"


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"  # Your detail template
    context_object_name = "book"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self):
        messages.success(self.request, "Book successfully created.")
        return redirect("record_list")

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error creating the book. Please check the details.",
        )
        return super().form_invalid(form)


# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self):
        messages.success(self.request, "Book successfully updated.")
        return redirect("record_list")

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error updating the book. Please check the details.",
        )
        return super().form_invalid(form)


class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"  # Your confirmation template
    success_url = reverse_lazy("book_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Book successfully deleted.")
        return super().delete(request, *args, **kwargs)
