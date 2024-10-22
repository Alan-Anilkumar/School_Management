from django.views.generic import TemplateView


class AdminDashboard(TemplateView):
    template_name = "admin/admin_dashboard.html"
