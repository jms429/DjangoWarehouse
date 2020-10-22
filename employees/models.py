from django.db import models

# Create your models here.

class Employee(models.Model):

    # Skill Level Choices
    class Level(models.IntegerChoices):
        NONE = 0
        BEGINNER = 1
        INTERMEDIATE = 2
        NOVICE = 3
        EXPERT = 4

    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='static/photos/', default='static/photos/default-photo.png')
    quality = models.IntegerField(choices=Level.choices, default=Level.NONE)
    engineering = models.IntegerField(choices=Level.choices, default=Level.NONE)
    press_brake = models.IntegerField(choices=Level.choices, default=Level.NONE)
    laser = models.IntegerField(choices=Level.choices, default=Level.NONE)
    water_jet = models.IntegerField(choices=Level.choices, default=Level.NONE)
    cnc_mill = models.IntegerField(choices=Level.choices, default=Level.NONE)
    cnc_lathe = models.IntegerField(choices=Level.choices, default=Level.NONE)
    stamp = models.IntegerField(choices=Level.choices, default=Level.NONE)
    drill = models.IntegerField(choices=Level.choices, default=Level.NONE)
    shipping = models.IntegerField(choices=Level.choices, default=Level.NONE)
    powder_coat = models.IntegerField(choices=Level.choices, default=Level.NONE)
    epoxy = models.IntegerField(choices=Level.choices, default=Level.NONE)
    weld = models.IntegerField(choices=Level.choices, default=Level.NONE)
    robot_weld = models.IntegerField(choices=Level.choices, default=Level.NONE)
    assembly = models.IntegerField(choices=Level.choices, default=Level.NONE)
    fuse = models.IntegerField(choices=Level.choices, default=Level.NONE)
    
    #sets name of admin table
    def __str__(self):
        return self.full_name  


class Event(models.Model):

    CERT = 'Certification'
    TIME = 'Time off'

    Event_Type_Choices = [
        (CERT , 'Certification'),
        (TIME , 'Scheduled time off'),
    ]

    name = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee name",)
    date = models.DateField()
    event_type = models.CharField(
        max_length=50,
        choices=Event_Type_Choices,
        default= CERT,
    )
         
class Department(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    color_hex = models.CharField(max_length=7, blank=True)
    icon_url = models.CharField(max_length=60, blank=True)
    level_1 = models.TextField(max_length=1500, blank=True)
    level_2 = models.TextField(max_length=1500, blank=True)
    level_3 = models.TextField(max_length=1500, blank=True)
    level_4 = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.name
