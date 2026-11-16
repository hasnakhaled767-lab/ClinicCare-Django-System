from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor, Patient, Appointment, MedicalRecord
from .forms import PatientForm, AppointmentForm, MedicalRecordForm


def dashboard(request):
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    pending_appointments = Appointment.objects.filter(status='Pending').count()
    recent_appointments = Appointment.objects.select_related('doctor', 'patient').all()[:8]

    context = {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'recent_appointments': recent_appointments,
    }
    return render(request, 'clinics/dashboard.html', context)


def patient_list(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(name__icontains=query) | Patient.objects.filter(phone__icontains=query)
    else:
        patients = Patient.objects.all()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تسجيل بيانات المريض بنجاح.')
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'clinics/patients.html', {'patients': patients, 'form': form, 'query': query})


def appointment_list(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            # التحقق من عدم وجود تضارب في نفس الموعد للطبيب
            conflict = Appointment.objects.filter(
                doctor=appointment.doctor,
                appointment_date=appointment.appointment_date,
                status='Pending'
            ).exists()
            if conflict:
                messages.error(request, 'عذراً، هذا الطبيب لديه موعد آخر محجوز في نفس التوقيت تماماً!')
            else:
                appointment.save()
                messages.success(request, 'تم حجز الموعد بنجاح.')
                return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'clinics/appointments.html', {'appointments': appointments, 'form': form})


def update_appointment_status(request, pk, status):
    appointment = get_object_or_404(Appointment, pk=pk)
    if status in ['Pending', 'Completed', 'Cancelled']:
        appointment.status = status
        appointment.save()
        messages.info(request, 'تم تحديث حالة الموعد.')
    return redirect('appointment_list')


def add_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    existing_record = MedicalRecord.objects.filter(appointment=appointment).first()

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=existing_record)
        if form.is_valid():
            record = form.save(commit=False)
            record.appointment = appointment
            record.save()
            appointment.status = 'Completed'
            appointment.save()
            messages.success(request, 'تم حفظ الروشتة والسجل الطبي بنجاح.')
            return redirect('view_prescription', record_id=record.id)
    else:
        form = MedicalRecordForm(instance=existing_record)

    return render(request, 'clinics/add_record.html', {
        'appointment': appointment,
        'form': form,
        'existing_record': existing_record
    })


def view_prescription(request, record_id):
    record = get_object_or_404(MedicalRecord, pk=record_id)
    return render(request, 'clinics/prescription.html', {'record': record})
