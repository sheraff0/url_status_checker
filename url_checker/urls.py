from django.contrib import admin
from django.urls import path, include
from url.views import url_list, request_url

urlpatterns = [
    path('', url_list),
    path('admin/', admin.site.urls),
    path('checkpoint/', include('django.contrib.auth.urls')),
    path("request-url/<pk>", request_url),
]
