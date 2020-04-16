from django.db import models

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    summary = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
   		return self.role

class Education(models.Model):
    course = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    score = models.CharField(max_length=25)
    duration = models.CharField(max_length=100)

    def __str__(self):
   		return self.course

class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
   		return self.skill

class Certification(models.Model):
    image = models.ImageField(upload_to='files/')
    certification = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='files/')

    def __str__(self):
   		return self.certification

class Achievement(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
   		return self.title