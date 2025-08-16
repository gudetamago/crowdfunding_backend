from django.db import models

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    owner_id = models.IntegerField()
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    campaign = models.ForeignKey(
        'Campaign',
        related_name='pledges',
        on_delete=models.CASCADE
    ) # we're not referring by ID... we just refer to the object