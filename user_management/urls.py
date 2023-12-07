from django.urls import path, include
from . import views

urlpatterns = [
  path("", include('allauth.urls') , name="allauth-urls"),
  path("profile/<int:id>/", views.profile_view, name="profile-view")
]