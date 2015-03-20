from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from photos.models import Photo

# Create your views here.
class ScheduleListView(TemplateView):
    template_name = 'schedule/schedule_list.html'

    @method_decorator
    def dispatch(self, *args, **kwargs):
        return super(ScheduleListView, self).dispatch(*args, **kwargs)

schedule_list = ScheduleListView.as_view()
