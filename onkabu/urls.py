from django.urls import path
from . import views

urlpatterns = [
  path('',views.Onkabu.as_view())
]