<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileUpdateForm
from user_management.models import UserProfile, GenerationDetails
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="accounts/login/")
def profile_view(request, id):
    userprofile = get_object_or_404(User, id=id)
    if request.user != userprofile:
        return redirect('/sdindex')
    
    update_form = UserProfileUpdateForm(instance=userprofile.profile)
    images_list = GenerationDetails.objects.filter(user=userprofile)
    print(images_list)
    print(userprofile)

    context =  {"userprofile": userprofile,
                "updateform": update_form,
                "images_list": images_list}
    return render(request, "userprofile/profile.html", context)
>>>>>>> Stashed changes
