from django.urls import path
from core import views

urlpatterns = [
  path("", views.index, name="index"),
  path("process_upload/", views.process_upload, name="process_upload")
]