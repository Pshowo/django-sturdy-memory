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
    ram_total = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    token = models.CharField(max_length=255, null=True)
    software_ver = models.CharField(max_length=11, null=True)

    def __str__(self):
        return str(self.number)

class Devices(models.Model):
    proj_num = models.ForeignKey(Project, on_delete=models.CASCADE)
    cpu = models.IntegerField()
    ram_used = models.DecimalField(max_digits=4, decimal_places=2)
    ram_percent = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)