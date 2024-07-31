from django import forms
from .models import Faculty, Department, ROLES, STATUS_CHOICES, C_TYPES, SEMESTER, Programme, Session, Course, Student


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_code', 'faculty_name']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_code', 'department_name', 'faculty']


class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['prog_name', 'department', 'status']

    def __init__(self, *args, **kwargs):
        super(ProgrammeForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = STATUS_CHOICES


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_code', 'session_name', 'status']

    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = STATUS_CHOICES


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_code', 'course_name', 'credit_unit', 'department', 'semester', 'level',
            'course_type', 'status'
        ]

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = STATUS_CHOICES
        self.fields['course_type'].choices = C_TYPES
        self.fields['semester'].choices = SEMESTER


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'registration_number', 'surname', 'first_name', 'middle_name', 'phone_number',
            'email', 'date_of_birth', 'programme', 'faculty', 'department'
        ]
