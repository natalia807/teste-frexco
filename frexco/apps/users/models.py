import string
import random

from django.db import models

from frexco.apps.core.models import TimestampedModel
from frexco.apps.core.utils import generate_random_password


class User(TimestampedModel):
    login = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    dateNasc = models.DateField()


    def save(self, *args, **kwargs):
        self.password =  generate_random_password()  if self.password is None  else self.password
        super(User, self).save(*args, **kwargs)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['login'], name="unique-login") ]
        indexes = [ models.Index(fields=['login']) ]