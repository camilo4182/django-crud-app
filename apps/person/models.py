from django.db import models

class Person(models.Model):
  id = models.AutoField(primary_key=True) # Primary key to uniquely identify a person
  first_name = models.CharField(max_length=100, unique=True) # First name of the person
  last_name = models.CharField(max_length=120, unique=True) # Last name of the person
  email = models.EmailField(max_length=200) # Email address of the person

  def __str__(self):
    return self.first_name
