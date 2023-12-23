from django.db import models


#USERS
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile = models.ImageField(upload_to='static/profiles/',nullable=True,blank=True)
    #latlong values
    # latitude=models.FloatField(nullable=True,blank=True)
    # latitude=models.FloatField(nullable=True,blank=True)
    location = models.PointField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id

#DISASTERS

class Earthquake(models.Model):
    earthquake_key=models.AutoField(primary_key=True)
    richter=models.FloatField(nullable=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(nullable=True,blank=True)
    loss=models.IntegerField(nullable=True,blank=True)
    #latlong values
    # latitude_epicenter=models.FloatField(nullable=True,blank=True)
    # longitude_epicenter=models.FloatField(nullable=True,blank=True)
    epicenter = models.PointField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.earthquake_key

class Flood(models.Model):
    FLOOD_CAUSES = [
        ('rainfall', 'Rainfall'),
        ('landslide', 'Landslide'),
        ('golf', 'Golf'),
        ('dam_failure', 'Dam Failure'),
        ('river_channel_changes', 'River Channel Changes'),
        ('other', 'Other'),
    ]
    flood_key=models.AutoField(primary_key=True)
    rainfall=models.FloatField(nullable=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(nullable=True,blank=True)
    loss=models.IntegerField(nullable=True,blank=True)
    #latlong values
    # latitude_epicenter=models.FloatField(nullable=True,blank=True)
    # longitude_epicenter=models.FloatField(nullable=True,blank=True)
    epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    cause = models.CharField(max_length=20, choices=FLOOD_CAUSES, default='rainfall')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.flood_key


class Glof(models.Model):
    GLOF_CAUSES= [
        ('avalanche', 'Avalanche'),
        ('earthquake', 'Earthquake'),
        ('dam_failure', 'Dam Failure'),
        ('other', 'Other'),
    ]
    glof_key=models.AutoField(primary_key=True)
    water_level=models.FloatField(nullable=True,blank=True)
    year=models.IntegerField()
    casualties=models.IntegerField(nullable=True,blank=True)
    cause = models.CharField(max_length=20, choices=GLOF_CAUSES, default='avalanche')
    loss=models.IntegerField(nullable=True,blank=True)
    #latlong values
    # latitude_epicenter=models.FloatField(nullable=True,blank=True)
    # longitude_epicenter=models.FloatField(nullable=True,blank=True)
    epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.glof_key

class Landslide(models.Model):
    LANDSLIDE_CAUSES= [
        ('earthquake', 'Earthquake'),
        ('rainfall', 'Rainfall'),
        ('soil_erosion', 'Soil Erosion'),
        ('other', 'Other'),
    ]
    landslide_key=models.AutoField(primary_key=True)
    year=models.IntegerField()
    casualties=models.IntegerField(nullable=True,blank=True)
    loss=models.IntegerField(nullable=True,blank=True)
    cause = models.CharField(max_length=20, choices=LANDSLIDE_CAUSES, default='rainfall')
    #latlong values
    # latitude_epicenter=models.FloatField(nullable=True,blank=True)
    # longitude_epicenter=models.FloatField(nullable=True,blank=True)
    epicenter = models.PointField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.earthquake_key
