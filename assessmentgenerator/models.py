from django.db import models
from django.contrib.auth.models import User
from django.dispatch import *
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    share = models.BooleanField(default=True)
    account_type = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username

class Subject(models.Model):
    subject = models.CharField(max_length= 30)

    def __unicode__(self):
        return self.subject

class Question(models.Model):
    creator = models.ForeignKey('UserProfile')
    created = models.DateTimeField(auto_now_add=True)
    question_type = models.CharField(max_length=1)
    question_text = models.CharField(max_length=300)
    question_body = models.CharField(max_length=1000)
    subject = models.CharField(max_length= 30,null=True)

    def __unicode__(self):
        ret = self.creator.user.username + ", " + str(self.created)
        return ret

#RECIEVER
@receiver(post_save, sender=User)
def add_user_profile(sender, **kwargs):
    UserProfile.objects.get_or_create(user=kwargs.get('instance'))
