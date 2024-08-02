from django.contrib import admin

from ResultSystem.models import Faculty, Department, Programme, Session, Course, Student, CourseAllocation, \
    StudentProgress, Attendance, CourseEnrolment, SemesterCourseResult, Result


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


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('prog_name', 'department', 'status')
    list_filter = ('prog_name', 'department')
    ordering = ('department',)
    search_fields = ('department',)


class SessionAdmin(admin.ModelAdmin):
    list_filter = ('session_code', 'session_name', 'status')
    list_display = ('session_code', 'session_name', 'status')
    ordering = ('session_name',)
    search_fields = ('session_name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'credit_unit', 'department', 'level',)
    list_filter = ('course_name', 'credit_unit')
    search_fields = ('course_code', 'course_name', 'level', 'semester')
    ordering = ('course_code', 'credit_unit')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'surname', 'first_name', 'email', 'programme', 'department')
    list_filter = ('registration_number', 'surname', 'programme')
    search_fields = ('registration_number', 'surname', 'first_name', 'middle_name')
    ordering = ('registration_number', 'surname')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'email', 'phone_number')
    list_filter = ('surname', 'programme', 'department')
    search_fields = ('surname', 'first_name', 'middle_name')
    ordering = ('surname', 'department')


class CourseAllocationAdmin(admin.ModelAdmin):
    list_display = ('course', 'staff', 'semester')
    list_filter = ('staff', 'semester')
    search_fields = ('course', 'staff')
    ordering = ('staff', 'semester')


class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_credit_registered')
    search_fields = ('student',)
    ordering = ('total_credit_earned',)
    list_filter = ('student',)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'attended')
    search_fields = ('student', 'course')
    ordering = ('attended',)
    list_filter = ('student',)


class CourseEnrolmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'session')
    search_fields = ('student', 'course')
    #ordering = ('course',)
    list_filter = ('session',)


class SemesterCourseResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'session', 'semester', 'level', 'total_score', 'grade')
    search_fields = ('student', 'course')
    #ordering = ('course',)
    list_filter = ('session',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'semester', 'level', 'gpa', 'carry_over')
    search_fields = ('student', 'course')
    #ordering = ('course',)
    list_filter = ('session',)


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(CourseAllocation, CourseAllocationAdmin)
admin.site.register(StudentProgress, StudentProgressAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(CourseEnrolment, CourseEnrolmentAdmin)
admin.site.register(SemesterCourseResult, SemesterCourseResultAdmin)
admin.site.register(Result, ResultAdmin)
