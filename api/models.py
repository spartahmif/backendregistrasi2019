from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    nim = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=10)
    gender = models.IntegerField()
    birth_place = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    line = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15) 
    address_home = models.CharField(max_length=100)
    address_local = models.CharField(max_length=100)
    disease = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=40)
    guardian_name = models.CharField(max_length=30)
    guardian_rel = models.CharField(max_length=15)
    guardian_mobile = models.CharField(max_length=15)
    consent = models.BooleanField()

    def __str__(self):
        return self.name