from django.urls import path
from core import views

urlpatterns = [
  path("", views.home, name="index"),
  path("replicateindex/", views.replicateIndex, name="replicateIndex"),
  path("sdindex/", views.sdIndex, name="sdIndex"),
  path("stablediffuse/", views.sd_view, name="sd_view"),
  path("replicateApi/", views.replicate_view, name="run_replicate")
]