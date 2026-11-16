from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="حساب المستخدم")
    specialization = models.CharField(max_length=150, verbose_name="التخصص الطبي")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    bio = models.TextField(blank=True, null=True, verbose_name="نبذة عن الطبيب")

    class Meta:
        verbose_name = "طبيب"
        verbose_name_plural = "الأطباء"

    def __str__(self):
        full_name = self.user.get_full_name() or self.user.username
        return f"د. {full_name} ({self.specialization})"


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    )
    name = models.CharField(max_length=150, verbose_name="اسم المريض")
    phone = models.CharField(max_length=20, unique=True, verbose_name="رقم الهاتف")
    age = models.PositiveIntegerField(verbose_name="العمر")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="الجنس")
    medical_history = models.TextField(blank=True, null=True, verbose_name="التاريخ المرضي المسبق")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    class Meta:
        verbose_name = "مريض"
        verbose_name_plural = "المرضى"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('Completed', 'تم الكشف'),
        ('Cancelled', 'ملغي'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="الطبيب المعالج")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="المريض")
    appointment_date = models.DateTimeField(verbose_name="تاريخ ووقت الموعد")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="حالة الموعد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الحجز")

    class Meta:
        verbose_name = "موعد"
        verbose_name_plural = "المواعيد"
        ordering = ['-appointment_date']

    def __str__(self):
        return f"موعد {self.patient.name} مع {self.doctor} بتاريخ {self.appointment_date:%Y-%m-%d %H:%M}"


class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, verbose_name="الموعد المرتبط")
    diagnosis = models.TextField(verbose_name="التشخيص الطبي")
    prescription = models.TextField(verbose_name="الروشتة / الأدوية المكتوبة")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات إضافية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "سجل طبي / روشتة"
        verbose_name_plural = "السجلات الطبية والروشتات"

    def __str__(self):
        return f"سجل طبي للمريض: {self.appointment.patient.name}"
