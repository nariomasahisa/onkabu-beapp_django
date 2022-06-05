from django.urls import path
from . import views

urlpatterns = [
  path('', views.CalcValue.as_view())
]