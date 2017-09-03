from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# User = settings.AUTH_USER_MODEL


STATUS_CHOICES = (
    ('P', 'Paid'),
    ('U', 'UNPAID'),
)


class Location(models.Model):
    place = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.place


class Users(models.Model):

    location = models.ForeignKey(Location, null=True)
    name = models.CharField(max_length=60)
    phone_number = models.IntegerField(default=0)
    price = models.PositiveIntegerField(blank=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES , default="U")
    descrition = models.TextField(
        help_text="write any description that will make yourlife easier ")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=datetime.now )
    expiry = models.DateTimeField( )

    #def clean(self):
    #   from django.core.exceptions import ValidationError
    #   if self.status = default="U":
    #       raise ValidationError('Start date cannot precede end date')
    #if self.status == 'draft' and self.pub_date is not None:
    #        raise ValidationError(_('Draft entries may not have a publication date.'))

    def save(self , *args, **kwargs):
        if self.expiry >= self.updated:
            self.status = "P"

        if self.updated >= self.expiry :
            if self.status == "U" :
                self.status = "U"
                self.expiry = default=self.updated+timedelta(days=30)
            else:
                self.status = default = "P"
                self.expiry = default=self.updated+timedelta(days=30)

        
            #self.expiry = default=self.updated+timedelta(days=1)
        
        super(Users, self).save(*args, **kwargs)

    #@property
    #def is_expired(self):
    #    if datetime.now > self.expiry_date:
    #        return True
    #    return False
   
    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.name
