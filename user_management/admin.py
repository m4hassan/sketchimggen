from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
# Register your models here.

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(UserProfile)