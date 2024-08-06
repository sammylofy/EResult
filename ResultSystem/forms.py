from django import forms
from .models import Faculty, Department, ROLES, STATUS_CHOICES, C_TYPES, SEMESTER, Programme, Session, Course, Student, \
    CourseEnrolment, Staff, SemesterCourseResult, CourseAllocation


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
        fields = ['registration_number', 'surname', 'first_name', 'middle_name', 'phone_number', 'email',
                  'date_of_birth', 'programme', 'faculty', 'department', 'status']
        # widgets ={
        #     'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        # }
        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'programme': forms.Select(attrs={'class': 'form-control', 'id': 'programme'}),
            'faculty': forms.Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['registration_number', 'surname', 'first_name', 'middle_name', 'phone_number', 'email',
                  'date_of_birth', 'programme', 'faculty', 'department', 'status']
        # widgets ={
        #     'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        # }
        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'programme': forms.Select(attrs={'class': 'form-control', 'id': 'programme'}),
            'faculty': forms.Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['registration_number'].widget.attrs['readonly'] = True


class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrolment
        fields = [
            'course', 'student', 'session'
        ]


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'staff_id', 'surname', 'first_name', 'middle_name', 'phone_number',
            'faculty', 'department', 'email'
        ]


class SemesterCourseResultForm(forms.ModelForm):
    class Meta:
        model = SemesterCourseResult
        fields = [
            'student', 'session', 'semester', 'level', 'course', 'practicals_score',
            'test_score', 'exam_score'
        ]


class CourseAllocationForm(forms.ModelForm):
    class Meta:
        model = CourseAllocation
        fields = [
            'staff', 'course', 'session', 'semester'
        ]
