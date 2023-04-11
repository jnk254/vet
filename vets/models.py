from django.db import models

# Create your models here.




class Member(models.Model):
    FirstName = models.CharField(max_length=200)
    SecondName = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Contact = models.IntegerField()
    Gender = models.CharField(max_length=7)
    NextofkinName = models.CharField(max_length=200)
    NextofkinContact = models.IntegerField()
    Age = models.IntegerField() 
    Address = models.TextField(max_length=100)
    District = models.CharField(max_length=50)
    
    class Meta:
       db_table="member"
        
    
class Baptism(models.Model):
    BaptismNo = models.IntegerField()
    
    class Meta:
        db_table="baptism"
        
class Communicant(models.Model):
    CommunicantNo = models.IntegerField()
    
    class Meta:
        db_table="communicant"
  
  #testt table      
class Emp(models.Model):
    emp_name = models.TextField()
    emp_email = models.EmailField()
    emp_mobile = models.TextField()

