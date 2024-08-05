from django.shortcuts import render, get_object_or_404, redirect
from .forms import FacultyForm, DepartmentForm, ProgrammeForm, SessionForm, CourseForm, StudentForm, StaffForm, \
    EditStudentForm
from django.contrib import messages
from .models import Faculty, Department, Programme, Session, Course, Student, Staff
from django.http import JsonResponse


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


def addStudent(request):
    title = "Student Registration"
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            surname = form.cleaned_data['surname']
            firstname = form.cleaned_data['first_name']
            messages.success(request, f"{surname}, {firstname} Registration Was Successful")
            return redirect('add_student')
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


def editStudent(request, idk):
    title = "Edit Student"
    student = get_object_or_404(Student, pk=idk)

    if request.method == "POST":
        form = EditStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f"{student.surname}, {student.first_name} {student.middle_name} Was Updated Successfully")
            return redirect('all_student')
    else:
        form = EditStudentForm(instance=student)

    context = {'title': title, 'form': form, 'student': student}
    return render(request, 'edit_student.html', context)


def deleteStudent(request, idk):
    student_instance = get_object_or_404(Student, pk=idk)
    if request.method == "POST":
        student_instance.delete()
        return redirect('all_student')
    return render(request, 'confirm_delete.html', {'student_instance': student_instance})


def load_departments(request):
    programme_id = request.GET.get('programme_id')
    print(f"Programme ID: {programme_id}")  # Debugging line
    departments = Department.objects.filter(programme__id=programme_id).values('id',
                                                                               'department_name') if programme_id else []
    return JsonResponse(list(departments), safe=False)


def load_faculties(request):
    department_id = request.GET.get('department_id')
    print(f"Department ID: {department_id}")  # Debugging line
    faculties = Faculty.objects.filter(department__id=department_id).values('id',
                                                                            'faculty_name') if department_id else []
    return JsonResponse(list(faculties), safe=False)


def addStaff(request):
    title = "Add Staff"
    if request.method == "POST":
        form = StaffForm(request.POST)  # Pass request.POST to the form
        cleaned = form.cleaned_data
        if form.is_valid():
            surname = cleaned['surname']
            firstname = cleaned['first_name']
            form.save()
            messages.success(request, f"{surname}, {firstname} added successfully")
            return redirect('add_staff')  # Redirect to avoid re-posting form on refresh
        else:
            print(form.errors)  # Print form errors to the console
            messages.error(request, "Failed to add staff. Please correct the errors below.")
    else:
        form = StaffForm()

    return render(request, 'add_staff.html', context={'title': title, 'form': form})


def viewAllStaff(request):
    title = "View All Staffs"
    staffs = Staff.objects.all()
    context = {'title': title, 'staffs': staffs}
    return render(request, 'view_staffs.html', context)


def getStaff(request, idk):
    title = "View Staff"
    staff = get_object_or_404(Staff, pk=idk)
    return render(request, 'staff.html', context={'title': title, 'staff': staff})


def editStaff(request, idk):
    title = "Edit Staff"
    staff = get_object_or_404(Staff, pk=idk)

    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f"{staff.surname}, {staff.first_name} {staff.middle_name} Was Updated Successfully")
            return redirect('all_staff')
    else:
        form = StaffForm(instance=staff)
    context = {'title': title, 'form': form, 'staff': staff}
    return render(request, 'edit_staff.html', context)


# def deleteStaff(request, idk):
#     staff_instance = get_object_or_404(Staff, pk=idk)
#     if request.method == "POST":
#         staff_instance.delete()
#         return redirect('all_staff')
#     return render(request, 'confirm_delete.html', {'staff_instance': staff_instance})

def deleteStaff(request, idk):
    if request.method == "POST":
        staff_instance = get_object_or_404(Staff, pk=idk)
        staff_instance.delete()
        messages.success(request, "Staff record deleted successfully.")
        return redirect('all_staff')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('all_staff')