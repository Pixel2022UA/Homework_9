from django.db import models


class PhoneNumber(models.Model):
    number = models.IntegerField()
