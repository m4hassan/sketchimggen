from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_management.models import UserProfile
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
