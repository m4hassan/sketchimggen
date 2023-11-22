from django.urls import path
from core import views

urlpatterns = [
  path("", views.index, name="index"),
  path("sdindex/", views.sdIndex, name="sdIndex"),
  path("stablediffuse/", views.sd_view, name="sd_view"),
  path("process_upload/", views.process_upload, name="process_upload")
]