from django.db import models


class CD(models.Model):
    name = models.CharField(max_length=50)


class Song(models.Model):
    name = models.CharField(max_length=50)
    cd = models.ForeignKey(CD, on_delete=models.CASCADE, blank=False, null=False)
