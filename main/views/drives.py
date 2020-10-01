from ..models import (
    Drive,
    State
)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from django.views.generic.detail import SingleObjectMixin
from django.views.generic import (
    ListView,
    DetailView,
)


class IndexView(ListView):
    model = Drive
    template_name = "main/drives/index.html"
    pk_url_kwarg = "cam_pk"


class DriveView(DetailView):
    model = Drive
    template_name = "main/drives/page.html"
    pk_url_kwarg = "cam_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get Drive State object
        drive_slug = self.kwargs["slug"]
        drive = Drive.objects.get(slug=drive_slug)
        context["state"] = State.objects.filter(abbr=drive.state)[0]
        return context
