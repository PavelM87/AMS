from django.shortcuts import render, reverse
from django.views import generic

from .forms import AMSModelForm
from .models import AMS
from users.mixins import SuperuserAndLoginRequiredMixin, GuestAccessMixin, ModeratorAndLoginRequiredMixin


class AMSListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "ams/ams_list.html"
    queryset = AMS.objects.all()
    context_object_name = "ams_objects"


class AMSDetailView(generic.DetailView):
    template_name = "ams/ams_detail.html"
    queryset = AMS.objects.all()
    context_object_name = "ams"


class AMSCreateView(SuperuserAndLoginRequiredMixin, generic.CreateView):
    template_name = "ams/ams_create.html"
    form_class = AMSModelForm

    def get_success_url(self):
        return reverse("ams:ams-list")


class AMSUpdateView(SuperuserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "ams/ams_update.html"
    queryset = AMS.objects.all()
    form_class = AMSModelForm

    def get_success_url(self):
        return reverse("ams:ams-list")


class AMSDeleteView(SuperuserAndLoginRequiredMixin, GuestAccessMixin, generic.DeleteView):
    template_name = "ams/ams_delete.html"
    queryset = AMS.objects.all()

    def get_success_url(self):
        return reverse("ams:ams-list")
