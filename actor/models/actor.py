from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=220, blank=False, null=False)
    birthday = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')

    def __str__(self):
        return self.name