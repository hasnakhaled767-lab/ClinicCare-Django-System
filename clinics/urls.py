from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/status/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
    path('appointments/<int:appointment_id>/record/', views.add_medical_record, name='add_medical_record'),
    path('prescription/<int:record_id>/', views.view_prescription, name='view_prescription'),
]
