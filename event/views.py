''' imports '''
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Event, Tag
from .forms import EventForm, CommentForm


class EventList(ListView):
    ''' Homepage View '''
    model = Event
    queryset = Event.objects.filter(status=1).order_by("start_date")
    template_name = "index.html"
    paginate_by = 6


class SearchResultsView(ListView):
    ''' Search Results '''
    model = Event
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Event.objects.filter(
            Q(title__icontains=query) | Q(owner__username__icontains=query)
        )
        return object_list


class EventDetail(DetailView):
    ''' View for the Event Details '''
    model = Event
    template_name = "event.html"
    form = CommentForm

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetail, self).get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        comments = event.comments.all
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True

        joined = False
        if event.characters.filter(created_by=self.request.user).exists():
            joined = True

        context['comments'] = comments
        context['comment_form'] = comment_form
        context['liked'] = liked
        context['joined'] = joined
        return context

    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse("event_detail", args=[str(pk)]))


def LikeView(request, pk):
    ''' The Like function on Event Details '''
    event = get_object_or_404(Event, id=request.POST.get("event_id"))
    if event.likes.filter(id=request.user.id).exists():
        event.likes.remove(request.user)
    else:
        event.likes.add(request.user)

    return HttpResponseRedirect(reverse("event_detail", args=[str(pk)]))


def JoinView(request, pk, *args, **kwargs):
    ''' The function on Event Details to join an Event'''
    select_event = get_object_or_404(Event, pk=pk)
    if select_event.characters.filter(id=request.POST.get("character_id")).exists():
        select_event.characters.remove(request.POST.get("character_id"))
    else:
        select_event.characters.add(request.POST.get("character_id"))

    return HttpResponseRedirect(reverse("event_detail", args=[str(pk)]))


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
    tagged_events = Event.objects.filter(tag__tag=tags.replace('-', ' ')).order_by("start_date")
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
