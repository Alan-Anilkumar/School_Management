from django.views.generic import TemplateView


class StaffDashboard(TemplateView):
    template_name = "staff/staff_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "staff Dashboard"
        return context
