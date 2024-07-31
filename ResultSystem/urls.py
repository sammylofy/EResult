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
]