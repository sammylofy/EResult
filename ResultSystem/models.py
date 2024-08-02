from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = [
    ('0', 'Disabled'),
    ('1', 'Active')
]
SEMESTER = [
    ('1', '1'),
    ('2', '2')
]
C_TYPES = [
    ('Elective', 'Elective'),
    ('Prerequisite', 'Prerequisite'),
    ('Normal', 'Normal')
]
ROLES = [
    ('Admin', 'Admin'),
    ('Lecturer', 'Lecturer'),
    ('Exam_Officer', 'Exam Officer'),
    ('HOD', 'Head of Department'),
    ('Student', 'Student')
    # add other roles
]


class Faculty(models.Model):
    faculty_code = models.CharField(max_length=20, unique=True)
    faculty_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.faculty_name}"

    class Meta:
        db_table = "faculty"


class Department(models.Model):
    department_code = models.CharField(max_length=20, unique=True)
    department_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department_name}"

    class Meta:
        db_table = "department"


class Programme(models.Model):
    prog_name = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.prog_name}"

    class Meta:
        db_table = "programme"


class Session(models.Model):
    session_code = models.CharField(max_length=20, unique=True)
    session_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.session_code} {self.status}"

    class Meta:
        db_table = "session"


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True, primary_key=True)
    course_name = models.CharField(max_length=100)
    credit_unit = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    level = models.CharField(max_length=20)
    course_type = models.CharField(max_length=100, choices=C_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return f"{self.course_code} {self.course_name}"

    class Meta:
        db_table = "courses"


class Student(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    date_of_birth = models.DateField()
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.registration_number} {self.surname} {self.first_name}"

    class Meta:
        db_table = "student"


class StudentProgress(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_credit_registered = models.IntegerField(default=0)
    total_credit_earned = models.IntegerField(default=0)
    total_credit_required = models.IntegerField(default=72)

    class Meta:
        db_table = "student_progress"


class Staff(models.Model):
    staff_id = models.CharField(max_length=45, unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.staff_id} {self.surname} {self.first_name}"

    class Meta:
        db_table = "staff"


class CourseAllocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_allocation"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    date = models.DateField()  # Date of attendance
    attended = models.BooleanField(default=False)  # True if student attended
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "attendance"


class CourseEnrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_enrolment"


class SemesterCourseResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    level = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Changed from CourseEnrolment
    practicals_score = models.DecimalField(max_digits=5, decimal_places=2)
    test_score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    grade_weight = models.DecimalField(max_digits=5, decimal_places=2)
    credit_unit_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
    credit_earned = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course_results"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    level = models.CharField(max_length=20)
    tcr = models.IntegerField(default=0)
    tce = models.IntegerField(default=0)
    total_credit_grade_points = models.IntegerField(default=0)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    carry_over = models.CharField(max_length=100)
    remarks = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "results"


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
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "objective_questions"


class ObjectivesAnswers(models.Model):
    question = models.ForeignKey(ObjectivesQuestions, on_delete=models.CASCADE)
    correct_option = models.CharField(max_length=1)
    answer = models.TextField()

    class Meta:
        db_table = "objective_answers"


class SubjectiveQuestions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    question = models.TextField()

    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "subjective_questions"


class SubjectiveAnswer(models.Model):
    question = models.ForeignKey(SubjectiveQuestions, on_delete=models.CASCADE)
    expected_answer = models.TextField()

    class Meta:
        db_table = "subjective_answer"


class GeneralEssayQuestions(models.Model):
    questions = models.TextField()
    assigned_marks = models.DecimalField(max_digits=5, decimal_places=2)
    level = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "general_questions"


class GeneralEssayAnswer(models.Model):
    question = models.ForeignKey(GeneralEssayQuestions, on_delete=models.CASCADE)
    expected_answer = models.TextField()

    class Meta:
        db_table = "general_essay_answer"  # Changed from "subjective_answer"


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


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "role"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

    class Meta:
        db_table = "user_profile"
