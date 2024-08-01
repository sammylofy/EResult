from django.shortcuts import render, get_object_or_404
from .forms import FacultyForm, DepartmentForm, ProgrammeForm, SessionForm, CourseForm, StudentForm
from django.contrib import messages
from .models import Faculty, Department, Programme, Session, Course, Student


# Create your views here.


def index(request):
    title = "Home"
    context = {'title': title}

    return render(request, 'index.html', context)


def addFaculty(request):
    title = "Add Faculty"
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty added successfully')
        else:
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', context={'title': title, 'form': form})


def viewAllFaculty(request):
    title = "All Faculties"
    faculties = Faculty.objects.all()
    context = {'title': title, 'faculties': faculties}
    return render(request, 'view_faculties.html', context)


def getFaculty(request, id):
    title = "Faculty"
    faculty = get_object_or_404(Faculty, pk=id)
    context = {'title': title, 'faculty': faculty}
    return render(request, 'faculty.html', context)


def addDepartment(request):
    title = "Add Department"
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added Successfully')
        else:
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', context={'title': title, 'form': form})


def viewAllDepartment(request):
    title = "All Department"
    departments = Department.objects.all()
    context = {'title': title, 'departments': departments}
    return render(request, 'view_departments.html', context)


def getDepartment(request, id):
    title = "Department"
    department = get_object_or_404(Department, pk=id)
    context = {'title': title, 'department': department}
    return render(request, 'department.html', context)


def addProgramme(request):
    title = "Add Programme"
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program added Successfully')
        else:
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = ProgrammeForm()
    return render(request, 'add_programme.html', context={'title': title, 'form': form})


def viewAllProgramme(request):
    title = "All Programme"
    programmes = Programme.objects.all()
    context = {'title': title, 'programmes': programmes}
    return render(request, 'view_programmes.html', context)


def getProgramme(request, id):
    title = "Programme"
    programme = get_object_or_404(Programme, pk=id)
    context = {'title': title, 'programme': programme}
    return render(request, 'programme.html', context)


def addSession(request):
    title = "Add Session"
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Session Added Successfully")
        else:
            messages.error(request, "Session Wasn't Added Successfully")
    else:
        form = SessionForm()
    return render(request, 'add_session.html', context={'title': title, 'form': form})


def viewAllSession(request):
    title = "View All Sessions"
    sessions = Session.objects.all()
    context = {'title': title, 'sessions': sessions}
    return render(request, 'view_sessions.html', context)


def getSession(request, id):
    title = "Session"
    session = get_object_or_404(Session, pk=id)
    context = {'title': title, 'session': session}
    return render(request, 'session.html', context)


def addCourse(request):
    title = "Add Courses"
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
        else:
            messages.error(request, "Adding Course Failed")
    else:
        form = CourseForm()
    return render(request, 'add_course.html', context={'title': title, 'form': form})


def viewAllCourses(request):
    title = "View All Courses"
    courses = Course.objects.all()
    context = {'title': title, 'courses': courses}
    return render(request, 'view_courses.html', context)


def getCourse(request, idk):
    title = "Course"
    course = get_object_or_404(Course, pk=idk)
    context = {'title': title, 'course': course}
    return render(request, 'course.html', context)


def add_student(request):
    title = "Student Registration"
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Registration Was Successful')
        else:
            messages.error(request, "Student Registration Failed")
    else:
        form = StudentForm()
    return render(request, 'add_student.html', context={'title': title, 'form': form})


def viewAllStudent(request):
    title = "View All Students"
    students = Student.objects.all()
    context = {'title': title, 'students': students}
    return render(request, 'view_students.html', context)


def getStudent(request, idk):
    title = "Student"
    student = get_object_or_404(Student, pk=idk)
    context = {'title': title, 'student': student}
    return render(request, 'student.html', context)
