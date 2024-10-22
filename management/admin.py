from django.contrib import admin
from .models import Department, Grade, FeeRecord

admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(FeeRecord)
