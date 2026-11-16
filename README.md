# ClinicCare - نظام إدارة العيادات والمراكز الطبية (Django)

نظام متكامل لإدارة العيادات الطبية، تسجيل بيانات المرضى، حجز المواعيد مع منع التضارب الزمني، وإصدار الروشتات الطبية القابلة للطباعة أو الحفظ بصيغة PDF.

## المميزات الرئيسية (Features)
- **لوحة تحكم إحصائية (Dashboard):** عرض إجمالي الأطباء، المرضى، المواعيد، وحالات الكشف.
- **إدارة المرضى (Patients Management):** تسجيل بيانات المرضى، التاريخ المرضي، والبحث السريع بالاسم أو رقم الهاتف.
- **نظام حجز المواعيد (Appointment Scheduling):** جدولة المواعيد ومنع حجز موعدين لنفس الطبيب في نفس التوقيت.
- **السجل الطبي والروشتة الإلكترونية (E-Prescription):** كتابة التشخيص والأدوية لكل زيارة وتوليد روشتة جاهزة للطباعة أو التصدير كـ PDF.
- **لوحة إدارة متكاملة (Django Admin):** لإدارة حسابات الأطباء والصلاحيات بسهولة.

## التقنيات المستخدمة (Tech Stack)
- **Backend:** Python, Django
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5 (RTL)

## طريقة التشغيل محلياً (Installation & Setup)

1. فك الضغط عن مجلد المشروع وافتحه في VS Code أو Terminal:
   ```bash
   cd clinic_management_system
   ```

2. إنشاء وتفعيل البيئة الافتراضية (Virtual Environment):
   ```bash
   python -m venv venv
   # على Windows:
   venv\Scripts\activate
   # على Mac/Linux:
   source venv/bin/activate
   ```

3. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```

4. تجهيز قاعدة البيانات وإنشاء حساب المدير (Superuser):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. تشغيل السيرفر المحلي:
   ```bash
   python manage.py runserver
   ```

6. افتح المتصفح على الرابط: `http://127.0.0.1:8000/`
   - ادخل أولاً إلى `http://127.0.0.1:8000/admin/` لإضافة بيانات **طبيب (Doctor)**، ثم ابدأ بتسجيل المرضى وحجز المواعيد من الواجهة الرئيسية.
