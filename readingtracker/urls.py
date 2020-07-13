from django.urls import path
from . import views


urlpatterns = [
    path('', views.PlanList.as_view(), name='list'),
    path('new/', views.CreatePlan.as_view(), name='add'),
    path('<int:pk>/', views.PlanDetail.as_view(), name='details'),
    path('<int:pk>/delete/', views.PlanDelete.as_view(), name='delete'),
    path('<int:pk>/update/', views.PlanUpdate.as_view(), name='update'),
]