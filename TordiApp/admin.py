from django.contrib import admin
from .models import profile, profile_pic, WalletBalance

# Register your models here.
admin.site.register(profile)
admin.site.register(profile_pic)
admin.site.register(WalletBalance)