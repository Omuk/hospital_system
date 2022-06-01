from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class Occupation(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self):
        return f"self.title"

class Physician(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/PhysicianImg', null=True, blank=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class CodeSpecialist(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/PhysicianImg', null=True, blank=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class Patient(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='profile_img/PhysicianImg', null=True, blank=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
