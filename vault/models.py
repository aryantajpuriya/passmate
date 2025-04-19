from django.db import models
from django.contrib.auth.models import User

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=100)
    website_url = models.URLField()
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.website_name} - {self.username}"


