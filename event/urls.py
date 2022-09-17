''' imports '''
from django.urls import path
from .views import EventList, EventDetail, CreateEvent, ConductView, EditEvent, DeleteEvent, TagsView, IndexTagsView, AddTag, LikeView, JoinView, SearchResultsView, HelpView

urlpatterns = [
    path("", EventList.as_view(), name="home"),
    path("event/<int:pk>", EventDetail.as_view(), name="event_detail"),
    path("create_event/", CreateEvent.as_view(), name="event_create"),
    path("event/edit/<int:pk>", EditEvent.as_view(), name="event_edit"),
    path("event/<int:pk>/remove", DeleteEvent.as_view(), name="event_delete"),
    path("tag/<str:tags>", TagsView, name="event_tag"),
    path("tag/index/", IndexTagsView.as_view(), name="index_tag"),
    path("tag/add/", AddTag.as_view(), name="add_tag"),
    path("conduct/", ConductView.as_view(), name="conduct"),
    path("help/", HelpView.as_view(), name="help"),
    path("like/<int:pk>", LikeView, name="event_like"),
    path("join/<int:pk>", JoinView, name="event_join"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]
