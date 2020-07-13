from django.views.generic import CreateView
import pyjokes

from .models import Plan
from .forms import PlanCreateForm


class CreatePlan(CreateView):
    model = Plan
    form_class = PlanCreateForm
    template_name = 'readingtracker/create_record.html'