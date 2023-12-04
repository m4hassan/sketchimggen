from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_management.models import UserProfile
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="accounts/login/")
def profile_view(request, username):
    userprofile = User.objects.get(username=username)
    print(userprofile)
    return render(request, "userprofile/profile.html", {"user": userprofile})