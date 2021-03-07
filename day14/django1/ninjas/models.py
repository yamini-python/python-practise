
from django.db import models

# Create your models here.


class Developer(models.Model):
    devName = models.CharField(max_length=80)
    experience = models.IntegerField(default=0)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.devName


class Skill(models.Model):
    skillName = models.CharField(max_length=50)
    level = models.IntegerField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.skillName
