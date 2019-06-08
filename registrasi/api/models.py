from django.db import models

# Create your models here.
class Student(models.Model):
    student_nim = models.CharField(max_length=8)
    student_name = models.TextField()
    student_nickname = models.CharField(max_length=10)
    student_gender = models.BooleanField()
    student_birthplace = models.CharField(max_length=30)
    student_birthdate = models.CharField(max_length=15)
    student_email = models.CharField(max_length=30)
    student_line = models.CharField(max_length=30)
    student_mobile = models.CharField(max_length=15) 

    def __str__(self):
        return self.student_name