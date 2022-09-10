''' imports '''
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from event.models import Profile, Event
from .forms import SignUpForm, EditUserSettingsForm, PasswordsChangeForm, ProfileForm, GM_PromotionForm


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    form = GM_PromotionForm

    def get_context_data(self, *args, **kwargs):
        profile_list = Profile.objects.all
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        gm_request_form = GM_PromotionForm()

        kwargs = super(ShowProfilePageView, self).get_context_data()
        gm_events = Event.objects.filter(game_master=kwargs['profile'])

        context['gm_request_form'] = gm_request_form
        context["kwargs"] = kwargs
        context["profile_list"] = profile_list
        context["gm_events"] = gm_events
        context["page_user"] = page_user
        return context

    def post(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        gm_request_form = GM_PromotionForm(data=request.POST)

        if gm_request_form.is_valid():
            gm_request_form.instance.name = request.user.username
            gm_request_form.instance.body = 'I would like to be a Game Master'
            gm_request_form.instance.requested = True
            gm_request = gm_request_form.save(commit=False)
            gm_request.profile = profile
            gm_request.save()
        else:
            gm_request_form = GM_PromotionForm()

        return HttpResponseRedirect(reverse('show_profile', args=[str(pk)]))


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = 'registration/password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/account_register.html'
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
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('home')
