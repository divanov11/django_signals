from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	first_name = models.CharField(max_length=200, null=True, blank=True)
	last_name = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return str(self.user)

