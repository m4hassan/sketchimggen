from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_management.models import GenerationDetails
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="/")
def profile_view(request, id):
    userprofile = get_object_or_404(User, id=id)
    if request.user != userprofile:
        return redirect('/sdindex')
    
    images_list = GenerationDetails.objects.filter(user=userprofile)

    images_list = reversed(images_list)

    context =  {"images_list": images_list}
    return render(request, "userprofile/profile.html", context)


