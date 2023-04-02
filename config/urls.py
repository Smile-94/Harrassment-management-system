
from django.contrib import admin
from django.urls import path
from django.urls import include

# For static files
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.conf import settings

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

# for serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, view=serve)
