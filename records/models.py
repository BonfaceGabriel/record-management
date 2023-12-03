import uuid
from django.db import models


class DigitalRoad(models.Model):
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('ongoing', 'Ongoing')
    )

    CHOICES = (
        ('publicwifi', 'Public Wifi'),
        ('lastmile', 'Last Mile'),
        ('backbone', 'Backbone')
    )

    id = models.AutoField(db_column='id') 
    record_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True) 
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    county = models.TextField(db_column='County', blank=True, null=True)  # Field name made lowercase.
    sub_county = models.TextField(db_column='Sub County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_of_site = models.TextField(db_column='Name of Site', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dsh_category = models.TextField(db_column='DSH Category',
                                    choices=CHOICES,
                                    blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_site= models.TextField(db_column='Type of Site', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status',
                            choices= STATUS_CHOICES,
                            default = 'ongoing', blank = True, null = True)  # Field name made lowercase.
    no_of_aps = models.IntegerField(db_column='No. of Aps', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_surveyed = models.DateField(db_column='Date Surveyed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_installed = models.DateField(db_column='Date Installed', blank=True, null=True, auto_now_add=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contractor = models.TextField(db_column='Contractor', blank=True, null=True)  # Field name made lowercase.
    boq_amount = models.IntegerField(db_column='BoQ Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inspection_status = models.TextField(db_column='Inspection status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inspection_date = models.DateField(db_column='Inspection Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return (f"{self.name_of_site}")
    
    class Meta:
        managed = True
        db_table = 'Digital-road'
