from django.db import models

class Device(models.Model):
    proj_num = models.IntegerField()
    cpu = models.IntegerField()
    ram_used = models.DecimalField(max_digits=4, decimal_places=2)
    ram_percent = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)