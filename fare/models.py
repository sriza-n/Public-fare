from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# user table
class User_Transaction_history(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_amount = models.FloatField(default=0.0)
    transaction_datetime = models.DateTimeField(auto_now_add=True)
    pickup_point_latitude = models.FloatField(null=True,blank=True)
    pickup_point_longitude = models.FloatField(null=True,blank=True)
    drop_point_latitude = models.FloatField(null=True,blank=True)
    drop_point_longitude = models.FloatField(null=True,blank=True)
    distance_covered = models.FloatField(null=True,blank=True)
    

    def __str__(self):
        return self.user.username

class User_amount(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    amount = models.FloatField(default=0.0)
    last_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



