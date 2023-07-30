from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
    

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(null = True, upload_to = 'images')
    designation = models.CharField(max_length=50, null = True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    career_objective = models.TextField()
    linkedin = models.URLField()
    github = models.URLField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Skill(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    skill = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.skill


class Education(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    start_year = models.BigIntegerField()
    end_year = models.BigIntegerField()
    education = models.CharField(max_length = 30)
    institute = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.education


class Experience(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length = 30)
    position = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.position}-{self.company}'


class Project(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    link1 = models.URLField(null = True, blank = True)
    link2 = models.URLField(null = True, blank = True)

    def __str__(self) -> str:
        return self.title