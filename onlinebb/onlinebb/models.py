from django.db import models



class Donor(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    blood_grp=models.CharField(max_length=5)
    location=models.CharField(max_length=25)
    ph_no = models.IntegerField()
    bld_pre = models.IntegerField()
    sugar_lvl = models.IntegerField()
    cholestrol = models.IntegerField()
    other = models.CharField(max_length=25)
