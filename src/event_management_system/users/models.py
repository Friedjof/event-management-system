from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import string
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField()
    company = models.CharField(max_length=100)
    over_18 = models.BooleanField()
    private_pin = models.CharField(max_length=100) # Second password/pin for e.g. doors or jitsi

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = Profile(user=instance)
            profile.over_18 = True
            profile.save()


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"{self.user.email} - {self.user.last_name} - {self.company}"

    def get_private_jitsi_url(self):
        return(f"https://jitsi.tux-tage.de/p_{self.surname}")
    
    def get_public_jitsi_url(self):
        return(f"https://jitsi.tux-tage.de/{self.surname}")

    def getUserRoleOfString(user_role_string):
        if user_role_string == 'CO':
            return Profile.UserRole.CONTACT
        elif user_role_string == 'AT':
            return Profile.UserRole.ATTENDANT
        elif user_role_string == 'OR':
            return Profile.UserRole.ORGANISATOR
        elif user_role_string == 'AD':
            return Profile.UserRole.ADMIN
        else:
            print(f"ERROR: getUserRoleOfString: no defined UserRole for {user_role_string}")
            return "Unknown!"

    def reset_password(self):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        
        password = []
        for i in range(20):
            password.append(random.choice(characters))

        random.shuffle(password)
        password_string = "".join(password)
        self.user.set_password(password_string)
        self.user.save()
        print(f"new password = {self.password}")