from django.views import View
from django.shortcuts import render, reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser, Team
from .forms import UserModelForm, TeamsModelForm
from users.mixins import SuperuserAndLoginRequiredMixin, ModeratorAndLoginRequiredMixin


class LandingPageView(View):

    def get(self, request):
        user = CustomUser.objects.all()
        context = {
            'user': user,
        }
        return render(request, 'landing.html', context)


class UserListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "users/users_list.html"
    queryset = CustomUser.objects.all()
    context_object_name = "users_objects"


class UserDetailView(SuperuserAndLoginRequiredMixin, generic.DetailView):
    template_name = "users/user_detail.html"
    queryset = CustomUser.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        try:
            context['team'] = Team.objects.get(member=kwargs['object'].id)
        except ObjectDoesNotExist:
            context['team'] = 'Не состоит'
        print(context)
        print(context['team'])
        return context


class UserCreateView(SuperuserAndLoginRequiredMixin, generic.CreateView):
    template_name = "users/user_create.html"
    form_class = UserModelForm

    def get_success_url(self):
        return reverse("users:users-list")


class UserUpdateView(SuperuserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "users/user_update.html"
    queryset = CustomUser.objects.all()
    form_class = UserModelForm

    def get_success_url(self):
        return reverse("users:users-list")


class UserDeleteView(SuperuserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "users/user_delete.html"
    queryset = CustomUser.objects.all()

    def get_success_url(self):
        return reverse("users:users-list")


class TeamCreateView(generic.CreateView):
    template_name = "users/team_create.html"
    form_class = TeamsModelForm

    def get_success_url(self):
        return reverse("users:users-list")
