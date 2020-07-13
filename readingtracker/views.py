from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy
import pyjokes

from .models import Plan
from .forms import PlanCreateForm


class CreatePlan(CreateView):
    model = Plan
    form_class = PlanCreateForm
    template_name = 'readingtracker/create_record.html'


class PlanDetail(DetailView):
    model = Plan
    template_name = 'readingtracker/detail.html'


class PlanList(ListView):
    model = Plan
    template_name = 'readingtracker/list.html'


class PlanDelete(DeleteView):
    model = Plan
    template_name = 'readingtracker/delete_confirm.html'
    success_url = reverse_lazy('list')