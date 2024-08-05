from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_faculty/', views.addFaculty, name='add_faculty'),
    path('all_faculty/', views.viewAllFaculty, name='all_faculty'),
    path('faculty/<int:id>/', views.getFaculty, name='get_faculty'),
    path('add_department/', views.addDepartment, name='add_department'),
    path('all_department/', views.viewAllDepartment, name='all_department'),
    path('department/<int:id>/', views.getDepartment, name='get_department'),
    path('add_programme/', views.addProgramme, name='add_programme'),
    path('all_programme/', views.viewAllProgramme, name='all_programme'),
    path('programme/<int:id>/', views.getProgramme, name='get_programme'),
    path('add_session/', views.addSession, name='add_session'),
    path('all_session/', views.viewAllSession, name='all_session'),
    path('session/<int:id>/', views.getSession, name='get_session'),
    path('add_staff/', views.addStaff, name='add_staff'),
    path('all_staff/', views.viewAllStaff, name='all_staff'),
    path('staff/<int:idk>/', views.getStaff, name='get_staff'),
    path('add_student/', views.addStudent, name='add_student'),
    path('all_student/', views.viewAllStudent, name='all_student'),
    path('student/<int:idk>/', views.getStudent, name='get_student'),
    path('edit_studet/<int:idk>/', views.editStudent, name='edit_student'),
    path('delete/<int:idk>/', views.deleteStudent, name = 'delete_student'),
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'),
    path('ajax/load-faculties/', views.load_faculties, name='ajax_load_faculties'),
]