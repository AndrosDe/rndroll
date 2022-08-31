from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Event
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
    #     max_player = event.character_max + 2
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
    #             "max_player": max_player,
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
