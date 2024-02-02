from django.db import models

class Registration(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Dob=models.DateField()
    Gender=models.CharField(max_length=100)
    Sclass=models.TextField()
    PhnNum=models.TextField(default=100)
    AdminScore=models.FloatField()
    Otp=models.TextField(default=100)
    class Meta:
        db_table="Registration"