
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("accounts.urls")),
    path("", include("authentication.urls")),
]
