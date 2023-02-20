from wsgiref.validate import validator
from .models import Appointment,Payment
from rest_framework import serializers
from datetime import date
from rest_framework.validators import UniqueTogetherValidator

class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','patientId','doctorId','patientName','doctorName','appointmentDate','appointment_slot']
        validator = [
            UniqueTogetherValidator(
                queryset=Appointment.objects.all(),
                fields=['appointmentDate','appointment_slot','doctorId']

            )
          ]
    # def validate(self, data):
    #     if data['appointmentDate'] < date.today():
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data
        
class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['appointment_id','card_number','expiry_date','CVV']
    def validate(self, data):
        if len(data['card_number'])<8 or len(data['card_number'])>16:
            raise serializers.ValidationError("provide proper card number")
        elif data['expiry_date'] < date.today():
            raise serializers.ValidationError("your card has bee expired")
        elif data['CVV'] == 3:
            raise serializers.ValidationError("Wrong CVV") 
        return data


