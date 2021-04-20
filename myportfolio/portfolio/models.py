from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.urls import reverse


class FrontendTechnologies(models.Model):
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.skills


class BackendTechnologies(models.Model):
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.skills


class Services(models.Model):
    service = models.CharField(max_length=255)

    def __str__(self):
        return self.service


class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    description = models.TextField()
    preview = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    review = models.CharField(max_length=255)
    project = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Packages(models.Model):
    PACKAGES = [
        ('b', 'BASIC'),
        ('s', 'STANDARD'),
        ('p', 'PREMIUM'),
    ]
    package = models.CharField(max_length=1, choices=PACKAGES, default='b')
    description = models.TextField()
    days = models.CharField(max_length=4)
    design_customization = models.BooleanField(default=False)
    content_management = models.BooleanField(default=False)
    responsive_design = models.BooleanField(default=False)
    source_code = models.BooleanField(default=False)
    pages = models.IntegerField()
    revisions = models.IntegerField()
    Total = models.IntegerField()

    def __str__(self):
        return self.package

