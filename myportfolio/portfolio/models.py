from django.db import models

# Create your models here.
from django.urls import reverse


class Services(models.Model):
    service = models.CharField(max_length=255)
    frontend_technologies = models.CharField(max_length=255)
    backend_technologies = models.CharField(max_length=255)

    def __str__(self):
        return self.service


class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(_(""), max_length=200)
    description = models.TextField()
    preview = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    review = models.CharField(max_length=255)
    project = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Packages(models.Model):
    PACKAGES = [
        ('b', 'BASIC'),
        ('s', 'STANDARD'),
        ('p', 'PREMIUM'),
    ]
    package = models.CharField(max_length=1, choices=PACKAGES, default='b')
    description = models.TextField()
    days = models.CharField(max_length=4)
    design_customization = models.BooleanField(default=True)
    responsive_design = models.BooleanField(default=True)
    source_code = models.BooleanField(default=True)
    revisions = models.BooleanField(default=True)

    def __str__(self):
        return self.package
