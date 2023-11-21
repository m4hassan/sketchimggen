# from allauth.account.forms import SignupForm, LoginForm
# from django import forms

# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, required=False, label='Last Name')
#     username = forms.CharField(max_length=30, required=False)
#     email = forms.EmailField(max_length=60, required=True, label="Email")

#     def signup(self, request, user):
#             user = super(CustomSignupForm, self).save(request)
#             user.first_name = self.cleaned_data['first_name']
#             user.last_name = self.cleaned_data['last_name']
#             user.username = self.cleaned_data['username']
#             user.email = self.cleaned_data['email']
#             user.save()

#             return user


# class CustomLoginForm(LoginForm):
    #   username = forms.CharField(max_length=30, label='Username')
    #   email = forms.EmailField(max_length=60, required=False, label='Email')

    #   def save(self, request):
    #         user = super(CustomSignupForm, self).save(request)
    #         user.username = self.cleaned_data['username']
    #         user.email = self.cleaned_data['email']
    #         user.save()

    #         return user
      
        