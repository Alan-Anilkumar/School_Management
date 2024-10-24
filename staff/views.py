from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from accounts.decorators import role_required


@method_decorator(
    role_required(
        allowed_roles=[
            "staff",
        ]
    ),
    name="dispatch",
)
class StaffDashboard(TemplateView):
    template_name = "staff/staff_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "staff Dashboard"
        return context
