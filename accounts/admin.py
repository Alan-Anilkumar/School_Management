from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Admin, Staff, Librarian, Student

admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Librarian)
admin.site.register(Student)
admin.site.register(Permission)
