from django.conf import settings
from django.db import models
from django_currentuser.middleware import ( get_current_user, get_current_authenticated_user )
from django_currentuser.db.models import CurrentUserField
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Friend(models.Model):
    """ 
        Friends that I owe
        name: name of the friend
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class OwnedModel(models.Model):
    """
        this object is owned by someone
        owner: the identity of the owner of a belongings
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=CurrentUserField())

    class Meta:
        abstract = True

class Belonging(OwnedModel):
    """ 
        what was burrowed. herits from OwnedModel 
        name: name of the object
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    """ 
        information about the exchange 
        what: what I burrowed
        to_who: to who I owe
        when: date of when it was burrowed
        returned: date of when it was returned
    
    """
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'the {what} was burrowed from {to_who}'.format(self.what,self.to_who) 