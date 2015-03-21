from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    share = models.BooleanField(default=True)
    account_type = models.IntegerField()

    def __unicode__(self):
        return self.user.username
