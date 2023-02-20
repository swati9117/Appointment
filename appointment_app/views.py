from cmath import e
from distutils.log import error
import http
import imp
from operator import ge
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from rest_framework import generics
from .serializers import AppointmentSerializers,PaymentSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from .models import Appointment, Payment
import json,jwt
from django.core import serializers

# Create your views 
class PatientAppointmentView(APIView):
    def get(self,_,pk=None):
        appointment = Appointment.objects.filter(patientId=pk)
        serializer = AppointmentSerializers(appointment,many=True)
        return Response(serializer.data)


        
class DoctorAppointmentView(APIView):
    def get(self,_,pk=None):
        appointment = Appointment.objects.filter(doctorId=pk)
        serializer = AppointmentSerializers(appointment,many=True)
        return Response(serializer.data) 

# class DoctorIDView(APIView):
#     def get(self,_,pk=None):
#         appointment = Appointment.objects.all()
#         serializer = AppointmentSerializers(appointment,many=True)
#         return Response(serializer.data)

class PaymentAppointmentView(APIView):
    def post(self,request,id):
        serializer = PaymentSerializers(data = request.data)
        try:
            stu = Appointment.objects.get(pk=id)
        except:
            return Response({'error':'invalid appointment id'})
        if int(request.data['appointment_id'])!= id:
            return Response({'msg':'check appointment ID'})
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            Appointment.objects.filter(pk=id).update(status=True)

            return Response({"message": "success"})
        return Response({'error':serializer.errors})
        

        
        
class AppointmentView(APIView):

    def post(self,request):
        serializer = AppointmentSerializers(data = request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response({"message": "success"})
            except:
                return Response({"message": "already booked"})

        return Response({'error':serializer.errors})

class AppointmentUpdateView(APIView):

    def put(self,request,pk):
        id = pk
        try:
            stu = Appointment.objects.get(pk=id)
            # old= Appointment.objects.filter(pk=id)
            # old_data = AppointmentSerializers(old,many=True).data

            # # old_data=json.dumps(old_data)
            # print()
        except:
            return Response({'errors':'this appointment does not exist and try to update another appointment id on your link'})
        serializer = AppointmentSerializers(stu,data=request.data)
        if int(request.data['id'])!=int(pk):
            return Response({'msg':'Given wrong appointment id'})
        # if old_data['status'] != request.data['status']:
        #     return Response({'msg':'you cannot change payment status , go to payment page.'})
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response({"message": "updated"})

                
            except:
                return Response({"message": "check for another date or slot"})
        return Response({'errors':serializer.errors})
    
   

    def delete(self,request,pk):
        id = pk
        try:
            stu = Appointment.objects.get(pk=id)

            if stu:
                operation = stu.delete()
                if operation:
                    return Response({'success':"deleted"})
                else:
                    return Response({'failed':" not deleted"})
        except:
            return Response({'failed':"id not found"})


# class Appointment     

class AddAppointment(APIView):
    def post(self,request,format=None):
        serializer = AppointmentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            appointment=serializer.save()
            return Response({'msg':'appointment data saved , complete payment'},status = status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.id for user in Appointment.objects.all()]
        return Response(usernames)







