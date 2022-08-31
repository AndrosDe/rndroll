from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event.urls'), name='event-urls'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name='member-urls'),
    path('summernote/', include('django_summernote.urls')),
]
