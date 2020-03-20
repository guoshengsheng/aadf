from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField("姓名", max_length=64)

class Role(models.Model):
    title = models.CharField("姓名", max_length=64)

class User(models.Model):
    name = models.CharField("姓名", max_length=64)
    department = models.ForeignKey('Department')
    role = models.ForeignKey('Role')