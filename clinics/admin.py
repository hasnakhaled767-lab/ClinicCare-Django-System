from django.contrib import admin
from .models import Doctor, Patient, Appointment, MedicalRecord


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'phone')
    search_fields = ('user__username', 'user__first_name', 'specialization')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'age', 'gender', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('gender',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    list_filter = ('status', 'doctor', 'appointment_date')
    search_fields = ('patient__name', 'doctor__user__username')


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'created_at')
    search_fields = ('appointment__patient__name', 'diagnosis')
