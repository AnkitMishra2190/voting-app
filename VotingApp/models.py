

from django.db import models


class Registration(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    userId = models.EmailField(max_length=50, unique=True, primary_key=True)
    passw = models.CharField(max_length=50)
    dob = models.CharField(blank=False, max_length=50)
    mobile = models.CharField(max_length=50)

    

    class Meta:
        db_table = "Registration"



class Vote(models.Model):

    candidate_politicalparties = models.CharField(max_length=50)
    # userId = models.ForeignKey(Registration, on_delete=models.CASCADE)
    userId = models.EmailField(max_length=50, unique=True)

    class Meta:
        db_table = "Vote"



class Admin2(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    userId = models.EmailField(max_length=50, unique=True, primary_key=True)
    passw = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    class Meta:
        
        db_table = "Admin2"

