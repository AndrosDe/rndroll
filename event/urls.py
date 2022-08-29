from django.urls import path
from .views import EventList, EventDetail

urlpatterns = [
    path("", EventList.as_view(), name="home"),
    path("<slug:slug>/", EventDetail.as_view(), name="event_detail"),
]