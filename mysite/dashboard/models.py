from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        return self.name

class Software(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    description = models.TextField(null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
