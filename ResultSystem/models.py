from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PROGRAMME = [
    ('OND', 'Ordinary Diploma'),
    ('ND', 'National Diploma'),
    ('HND', 'Higher National Diploma'),
    ('WKPG', 'Weekend Programme')
]

STATUS_CHOICES = [
    ('0', 'Disabled'),
    ('1', 'Active, not current'),
    ('2', 'Active, current')
]


class Faculty(models.Model):
    faculty_code = models.CharField(max_length=20, unique=True)
    faculty_name = models.CharField(max_length=100)

    class Meta:
        db_table = "faculty"


class Department(models.Model):
    department_code = models.CharField(max_length=20, unique=True)
    department_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        db_table = "department"


class Session(models.Model):
    session_code = models.CharField(max_length=20, unique=True)
    session_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        db_table = "session"


class Semester(models.Model):
    semester_code = models.CharField(max_length=20, unique=True)
    semester_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        db_table = "semester"


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True, primary_key=True)
    course_name = models.CharField(max_length=100)
    credit_unit = models.IntegerField(default=0)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    class Meta:
        db_table = "courses"


class Prerequisite(models.Model):
    prerequisite_code = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "prerequisite"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20, unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(maxlength=100, null=True, blank=True)
    phone_number = models.CharField(maxlength=11)
    email = models.EmailField()
    date_of_birth = models.DateField()
    programme = models.CharField(maxlength=20, choices=PROGRAMME)
    level = models.CharField(maxlength=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    status = models.CharField(maxlength=1, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "student_data"


class StudentProgress(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_credit_earned = models.IntegerField(default=0)
    total_credit_required = models.IntegerField(default=72)
    is_eligible_for_graduation = models.BooleanField(default=False)

    class Meta:
        db_table = "student_progress"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(maxlength=45, unique=True)
    surname = models.CharField(maxlength=100)
    first_name = models.CharField(maxlength=100)
    middle_name = models.CharField(maxlength=100, null=True, blank=True)
    phone_number = models.CharField(maxlength=11)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "staff"


class CourseAllocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_allocation"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date = models.DateField()  # Date of attendance
    attended = models.BooleanField(default=False)  # True if student attended

    class Meta:
        db_table = "attendance"


class CourseEnrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_enrolment"


class ExamEligibility(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    eligible = models.BooleanField(default=False)  # True if student is eligible for exam

    class Meta:
        db_table = "exam_eligibility"


class ScoreSheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.CharField(maxlength=20)
    credit_unit = models.IntegerField(default=0)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    practicals = models.DecimalField(max_digits=5, decimal_places=2)
    test_score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(maxlength=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "upload_course_scores"


class SemesterResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.CharField(maxlength=20)
    grade_weight = models.DecimalField(max_digits=5, decimal_places=2)
    credit_unit_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
    credit_earned = models.IntegerField(default=0)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "semester_results"


class ResultSummary(models.Model):
    registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    semester_result = models.ForeignKey(SemesterResult, on_delete=models.CASCADE)
    tcr = models.IntegerField(default=0)
    tce = models.IntegerField(default=0)
    total_credit_grade_points = models.IntegerField(default=0)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    lcgpa = models.DecimalField(max_digits=5, decimal_places=2)  # Last CGPA
    carry_over = models.CharField(max_length=100)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "result_summary"


"""
    Setting up exam model below, its not really clear on what I am to do now
    but I hope to get my line of thought straight soonest.
"""


class ObjectivesQuestions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "objective_questions"


class SubjectiveQuestions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    question = models.TextField()
    expected_answer = models.TextField()
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "subjective_questions"


class GeneralEssayQuestions(models.Model):
    questions = models.TextField()
    expected_answer = models.TextField()
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)
    level = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "general_questions"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    objectives = models.ForeignKey(ObjectivesQuestions, on_delete=models.CASCADE)
    subjectives = models.ForeignKey(SubjectiveQuestions, on_delete=models.CASCADE)
    essay_questions = models.ForeignKey(GeneralEssayQuestions, on_delete=models.CASCADE)
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "exam"
