from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE
    )
    # Below are extra fields that are not part of the requirements
    # alt_title = models.CharField(max_length=200)
    # alt_description = models.TextField()
    # alt_image = models.URLField()

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    campaign = models.ForeignKey(
        'Campaign',
        related_name='pledges',
        on_delete=models.CASCADE
    ) # we're not referring by ID... we just refer to the object
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges', # we're referring to the property of 'pledges' on the other side
        on_delete=models.CASCADE
    )
