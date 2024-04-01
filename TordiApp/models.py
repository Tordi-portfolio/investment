from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=25)
    Bio = models.CharField(max_length=250)
    Username = models.CharField(max_length=250)
    Email = models.EmailField(null=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name + ' ' + self.Username + ' ' + str(self.user) + ' ' + self.Bio + ' '  + self.Email + ' ' + self.location


class profile_pic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return self.profile_pic


class WalletBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Bicoin = models.DecimalField(max_digits=20, decimal_places=4)
    Etherium = models.DecimalField(max_digits=20, decimal_places=4)
    Usdt = models.DecimalField(max_digits=20, decimal_places=4)
    Dogecoin = models.DecimalField(max_digits=20, decimal_places=4)
    Bnb = models.DecimalField(max_digits=20, decimal_places=4)