from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_faculty/', views.addFaculty, name='add_faculty'),
    path('all_faculty/', views.viewAllFaculty, name='all_faculty'),
    path('faculty/<int:pk>/', views.getFaculty, name='get_faculty'),
    path('add_department/', views.addDepartment, name='add_department'),
    path('all_department/', views.viewAllDepartment, name='all_department'),
    path('department/<int:pk>/', views.getDepartment, name='get_faculty'),
    path('add_programme/', views.addProgramme, name='add_programme'),
    path('all_programme/', views.viewAllProgramme, name='all_programme'),
    path('programme/<int:pk>/', views.getProgramme, name='get_faculty'),
    path('add_session/', views.addSession, name='add_session'),
    path('all_session/', views.viewAllSession, name='all_session'),
    path('session/<int:pk>/', views.getSession, name='get_faculty'),
    path('add_staff/', views.addStaff, name='add_staff'),
    path('all_staff/', views.viewAllStaff, name='all_staff'),
    path('staff/<int:pk>/', views.getStaff, name='get_faculty'),
    path('add_student/', views.addStudent, name='add_student'),
    path('all_student/', views.viewAllStudent, name='all_student'),
    path('student/<int:pk>/', views.getStudent, name='get_faculty'),
]