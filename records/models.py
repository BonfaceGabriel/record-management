from django.db import models

# Create your models here.
class DigitalRoad(models.Model):
    id = models.IntegerField(db_column='id', blank=True, null=False, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    county = models.TextField(db_column='County', blank=True, null=True)  # Field name made lowercase.
    sub_county = models.TextField(db_column='Sub County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_of_site = models.TextField(db_column='Name of Site', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dsh_category = models.TextField(db_column='DSH Category', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_site = models.TextField(db_column='Type of site', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    no_of_aps = models.IntegerField(db_column='No. of Aps', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_surveyed = models.DateField(db_column='Date Surveyed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_installed = models.DateField(db_column='Date Installed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contractor = models.TextField(db_column='Contractor', blank=True, null=True)  # Field name made lowercase.
    boq_amount = models.IntegerField(db_column='BoQ Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inspection_status = models.TextField(db_column='Inspection status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inspection_date = models.DateField(db_column='Inspection Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Digital-road'
