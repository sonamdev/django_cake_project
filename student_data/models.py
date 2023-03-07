from django.db import models

class Coursedata(models.Model):
    course_id=models.CharField(primary_key=True,max_length=20)
    course_name=models.CharField(max_length=50)
    duration= models.CharField(max_length=20)

class Studentdata(models.Model):
    sid=models.CharField(primary_key=True,max_length=20)
    name= models.CharField(max_length=100)
    course= models.ForeignKey(Coursedata,on_delete=models.CASCADE)
