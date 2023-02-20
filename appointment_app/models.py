from enum import unique
from django.db import models


class Appointment(models.Model):
    time_slot=[
       ('9','9'),
       ('12','12'),
       ('3','3')
    ]
    patientId=models.PositiveIntegerField("patientId")
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.CharField(max_length=40,null=True)
    #appointmentDate=models.TimeField()
    appointment_slot =models.CharField(max_length=100,choices=time_slot,default='9' )
    #status=models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['appointmentDate','appointment_slot','doctorId'],name='already booked')
        ]


class Payment(models.Model):
    appointment_id = models.PositiveIntegerField(unique=True)
    card_number = models.CharField(max_length=191)
    expiry_date = models.DateField(auto_now_add=False,auto_now=False)
    CVV = models.CharField(max_length=4)