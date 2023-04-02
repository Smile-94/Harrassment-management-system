
from django.contrib import admin
from django.urls import path
from django.urls import include

from accounts import urls as accounts_urls
from authority import urls as authority_urls
from student import urls as student_urls
from report import urls as report_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(accounts_urls)),
    path("", include(authority_urls)),
    path("", include(student_urls)),
    path("", include(report_urls)),
]
