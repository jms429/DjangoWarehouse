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
    machine_1 = models.IntegerField(choices=Level.choices, default=Level.NONE)
    machine_2 = models.IntegerField(choices=Level.choices, default=Level.NONE)
    machine_3 = models.IntegerField(choices=Level.choices, default=Level.NONE)
    machine_4 = models.IntegerField(choices=Level.choices, default=Level.NONE)
    machine_5 = models.IntegerField(choices=Level.choices, default=Level.NONE)
    photo = models.ImageField(upload_to='static/photos/', default='static/photos/default-photo.png')
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
         


