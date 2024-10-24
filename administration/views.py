from django.views.generic import TemplateView

from accounts.models import Student, Staff, Admin, Librarian
from library.models import Book, LibraryRecord
from management.models import Department


class AdminDashboard(TemplateView):
    template_name = "admin/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Admin Dashboard"
        context['students_count'] = Student.objects.count()
        context['staff_count'] = Staff.objects.count()
        context['admin_count'] = Admin.objects.count()
        context['librarian_count'] = Librarian.objects.count()
        context['books_count'] = Book.objects.count()
        context['departments_count'] = Department.objects.count()
        context['books_to_return'] = LibraryRecord.objects.filter(status="BORROWED").count()
        return context
