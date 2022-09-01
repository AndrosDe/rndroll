from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Event, Tag
from .forms import EventForm


class EventList(ListView):
    ''' Homepage View '''
    model = Event
    queryset = Event.objects.filter(status=1).order_by("start_date")
    template_name = "index.html"
    paginate_by = 6


class EventDetail(DetailView):
    ''' View for the Event Details '''
    model = Event
    template_name = "event.html"

    # def get(self, request, *args, **kwargs):
    #     queryset = Event.objects.filter(status=1)
    #     event = get_object_or_404(queryset)
    #     characters = event.characters
    #     comments = event.comments
    #     liked = False
    #     if event.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     return render(
    #         request,
    #         "event.html",
    #         {
    #             "event": event,
    #             "characters": characters,
    #             "comments": comments,
    #             "commented": False,
    #             "liked": liked,
    #         },
    #     )


class CreateEvent(CreateView):
    ''' Creating an Event '''
    model = Event
    form_class = EventForm
    template_name = "event_create.html"


class EditEvent(UpdateView):
    ''' Updateing an Event '''
    model = Event
    form_class = EventForm
    template_name = "event_edit.html"


class DeleteEvent(DeleteView):
    ''' Deleting an Event '''
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("home")


class EventCalendar(TemplateView):
    ''' View for the Event Details '''
    model = Event
    template_name = "calendar.html"


class ConductView(TemplateView):
    ''' View for the Event Details '''
    model = Event
    template_name = "conduct.html"


def TagsView(request, tags):
    ''' View for the filtered Tags '''
    tagged_events = Event.objects.filter(tag__tag=tags.replace('-', ' '))
    return render(
        request, "tagged_events.html", {
            "tags": tags.replace('-', ' '), "tagged_events": tagged_events
            })


class IndexTagsView(ListView):
    ''' View for all Tags '''
    model = Tag
    tag_list = Tag.objects.all()
    template_name = "tag_index.html"


class AddTag(CreateView):
    ''' Creating a Tag '''
    model = Tag
    fields = '__all__'
    template_name = "tag_add.html"
    success_url = reverse_lazy("index_tag")
