from unicodedata import name
from django.db import models

# Create your models here.

class Tenants (models.Model):
    tenant_id = models.CharField(max_length=64,primary_key=True)
    name = models.CharField(max_length=64)
    phno = models.CharField(max_length=32)
    p_addr = models.CharField(max_length=128)
    govtid = models.CharField(max_length=32)
    roomno = models.CharField(max_length=8)
    rent = models.CharField(max_length=32)
    roomsharing = models.IntegerField()
    occupation = models.CharField(max_length=16)
    office_addr = models.CharField(max_length=128)
    office_id = models.CharField(max_length=16)
    from_date = models.DateField()
    to_date = models.DateField(default=None)
    advance = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


