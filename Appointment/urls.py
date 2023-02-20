"""Appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appointment_app.views import PatientAppointmentView,DoctorAppointmentView, AppointmentView,AppointmentUpdateView,PaymentAppointmentView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('appointments/',AddAppointment.as_view(),name='appointment'),
    path('payment/<int:id>/',PaymentAppointmentView.as_view(),name='payment'),
    path('Patient/<str:pk>/appointment/',PatientAppointmentView.as_view(),name='patient_appointment'),
    path('Doctor/<str:pk>/appointment/',DoctorAppointmentView.as_view(),name='doctor_appointment'),
  #  path('Doctor/docapp/',doctorappview.as_view(),name='doctor_appointment'),
  #  path('patient/app/',patientappview.as_view(),name='patient_appointment'),
    path('appointment_details/',AppointmentView.as_view(),name='appointment_details'),
    path('update_appointment_details/<int:pk>/',AppointmentUpdateView.as_view(),name='update_appointment_details')


    # path('appointment_details/',AppointmentView.as_view(),name='appointment_details')



]
