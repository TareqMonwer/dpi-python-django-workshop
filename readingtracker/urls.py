from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.CreatePlan.as_view(), name='add'),
]