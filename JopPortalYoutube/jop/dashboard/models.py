from django.db import models
from Appjob.models import *
from company.models import *
from resume.models import *
class Industry(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class JobType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField() # maaş
    requirements = models.TextField() # Gereksinimler
    ideal_candidate = models.TextField() # İdeal Aday Özellikleri
    is_available = models.BooleanField(default=True)
    addjob = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
    job_type =  models.ForeignKey(JobType, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

class ApplyJob(models.Model):
    status_choies = {
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending'),
    }
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=status_choies)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)