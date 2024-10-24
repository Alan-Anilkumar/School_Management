
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("administration/", include("administration.urls")),
    path("admin/", admin.site.urls),
    path("staff/", include("staff.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("library/", include("library.urls")),
    path("management/", include("management.urls")),
]
