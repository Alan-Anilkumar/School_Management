from django.views.generic import TemplateView

from accounts.models import Librarian, Staff, Student


class AdminDashboard(TemplateView):
    template_name = "admin/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_count'] = Staff.objects.count()  # Assuming you have a Staff model
        context['librarian_count'] = Librarian.objects.count()  # Assuming you have a Librarian model
        context['student_count'] = Student.objects.count()  # Assuming you have a Student model
        return context
