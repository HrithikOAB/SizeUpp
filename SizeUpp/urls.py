from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import invoice

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# =========================
# Swagger Configuration
# =========================

schema_view = get_schema_view(
    openapi.Info(
        title="SizeUpp API",
        default_version="v1",
        description="API documentation for SizeUpp",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@sizeupp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# =========================
# URL Patterns
# =========================

urlpatterns = [

    # Django Admin
    path("admin/", admin.site.urls),

    # =========================
    # REST APIs
    # =========================

    path("api/", include("authentication.urls")),
    path("api/product/", include("product.urls")),

    # =========================
    # Swagger
    # =========================

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),

    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),

    # =========================
    # Dashboard
    # =========================

    path("", include("dashboard.urls")),

    # Invoice
    path(
        "invoice/<slug:slug>",
        invoice,
        name="invoice",
    ),
]


# =========================
# Media files (development)
# =========================

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
