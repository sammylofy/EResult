from django.contrib import admin

from ResultSystem.models import Faculty, Department


# Register your models here.

class FacultyAdmin(admin.ModelAdmin):
    list_filter = ('faculty_name',)
    list_display = ('faculty_code', 'faculty_name')
    search_fields = ('faculty_name',)
    ordering = ('faculty_code',)

class DepartmentAdmin(admin.ModelAdmin):
    list_filter = ('department_code', 'department_name')
    list_display = ('department_code', 'department_name', 'faculty')
    search_fields = ('department_name',)
    ordering = ('department_code',)

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
