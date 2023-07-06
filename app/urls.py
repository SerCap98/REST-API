from django.urls import path
from .views import *


urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person_list'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('faculties/', FacultyListCreateView.as_view(), name='faculty_list'),
    path('faculties/<int:pk>/', FacultyDetailView.as_view(), name='faculty_detail'),
    path('schools/', SchoolListCreateView.as_view(), name='school_list'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('sections/', SectionListCreateView.as_view(), name='section_list'),
    path('sections/<int:pk>/', SectionDetailView.as_view(), name='section_detail'),
    path('section/<int:section_id>/students/', SectionStudentsList.as_view()),

    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('section/<int:section_id>/students/', SectionStudentsList.as_view(),name='section_students_list'),
    path('section/<int:section_id>/teachers/', SectionTeachersList.as_view(), name='section_teachers_list'),
    
]
