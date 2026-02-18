from django.db import models
from django.utils import timezone


# Create your models here.
now = timezone.now()


class User(models.Model):
    user_fname = models.CharField(max_length=255, verbose_name="First Name")
    user_lname = models.CharField(max_length=255, verbose_name="Last Name")
    user_email = models.EmailField(max_length=255, verbose_name="Email")
    user_position = models.CharField(max_length=11, verbose_name="Position")
    pub_date = models.DateTimeField(default=now, verbose_name="Public Date")

    def __str__(self):
        return self.user_fname