from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("event.urls"), name="event-urls"),
    path('summernote/', include('django_summernote.urls')),
]
