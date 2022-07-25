from django.db import models


# Create your models here.
class Tarea(models.Model):
    class Status(models.TextChoices):
        BACK = "1", "BACKLOG"
        TO = "2", "TO DO"
        DO = "3", "DOING"
        TEST = "4", "TEST"
        DONE = "5", "DONE"

    class Priority(models.TextChoices):
        HIGH = "1", "ALTA"
        MEDIUM = "2", "MEDIA"
        LOW = "3", "BAJA"

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.BACK)
    priority = models.CharField(max_length=1, choices=Priority.choices, default=Priority.LOW)
    date_of_delivery = models.DateTimeField()
    comments = models.CharField(max_length=500)
