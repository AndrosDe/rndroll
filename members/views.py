from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from event.models import Profile, Event
from character.models import Character
from .forms import SignUpForm, EditUserSettingsForm, PasswordsChangeForm, ProfileForm


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        profile_list = Profile.objects.all

        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        kwargs = super(ShowProfilePageView, self).get_context_data()
        kwargs.update({'user': self.request.user})

        created_characters = Character.objects.filter(created_by=kwargs['user'])
        owned_events = Event.objects.filter(owner=kwargs['user'])
        gm_events = Event.objects.filter(game_master=kwargs['profile'])
        joined_events = Event.objects.filter(characters__created_by=kwargs['user'])

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["kwargs"] = kwargs
        context["profile_list"] = profile_list
        context["joined_events"] = joined_events
        context["gm_events"] = gm_events
        context["owned_events"] = owned_events
        context["created_characters"] = created_characters
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = 'registration/password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditUserSettingsView(UpdateView):
    form_class = EditUserSettingsForm
    template_name = 'registration/profile_settings_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class EditProfilePageView (UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
