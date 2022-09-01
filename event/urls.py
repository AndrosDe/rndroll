from django.urls import path
from .views import EventList, EventDetail, CreateEvent, EventCalendar, ConductView, EditEvent, DeleteEvent, TagsView, IndexTagsView, AddTag, LikeView

urlpatterns = [
    path("", EventList.as_view(), name="home"),
    path("event/<int:pk>", EventDetail.as_view(), name="event_detail"),
    path("create_event/", CreateEvent.as_view(), name="event_create"),
    path("event/edit/<int:pk>", EditEvent.as_view(), name="event_edit"),
    path("event/<int:pk>/remove", DeleteEvent.as_view(), name="event_delete"),
    path("tag/<str:tags>", TagsView, name="event_tag"),
    path("tag/index/", IndexTagsView.as_view(), name="index_tag"),
    path("tag/add/", AddTag.as_view(), name="add_tag"),
    path("calendar/", EventCalendar.as_view(), name="event_calendar"),
    path("conduct/", ConductView.as_view(), name="conduct"),
    path("like/<int:pk>", LikeView, name="event_like"),
]
