from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, default='None')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=4)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def delete(self, *args, **kwargs):
        # Delete the associated User and then delete the Profile
        self.user.delete()
        super().delete(*args, **kwargs)

    def get_full_name(self):
        return self.user.get_full_name()

    def get_short_name(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'Profiles'
