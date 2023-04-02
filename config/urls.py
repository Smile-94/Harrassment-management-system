
from django.contrib import admin
from django.urls import path
from django.urls import include

from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(accounts_urls) ),
]
