from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Event


class EventList(generic.ListView):
    ''' Homepage View '''
    model = Event
    queryset = Event.objects.filter(status=1).order_by("start_date")
    template_name = "index.html"
    paginate_by = 6


class EventDetail(View):
    ''' View for the Event Details '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        characters = event.characters
        max_player = event.character_max + 2
        joined = False
        if event.characters.filter(id=self.request.user.id).exists():
            joined = True

        return render(
            request,
            "event.html",
            {
                "event": event,
                "characters": characters,
                "max_player": max_player,
                "joined": joined,
            },
        )