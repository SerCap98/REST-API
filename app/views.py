from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *



class EnabledObjectsMixin:
    def get_queryset(self):
        return self.queryset.filter(status='EN')
    
class PersonListCreateView(EnabledObjectsMixin,generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(EnabledObjectsMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class FacultyListCreateView(EnabledObjectsMixin,generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyDetailView(EnabledObjectsMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class SchoolListCreateView(EnabledObjectsMixin,generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetailView(EnabledObjectsMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SectionListCreateView(EnabledObjectsMixin,generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailView(EnabledObjectsMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class EnrollmentListCreateView(EnabledObjectsMixin,generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentDetailView(EnabledObjectsMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class SectionStudentsList(EnabledObjectsMixin, generics.ListAPIView):
    serializer_class = StudentEnrollmentSerializer
    queryset = Enrollment.objects.all()

    def get_queryset(self):

        queryset = super().get_queryset()
        section_id = self.kwargs.get('section_id')
        return queryset.filter(Section__id=section_id, type='student')
    

class SectionTeachersList(EnabledObjectsMixin, generics.ListAPIView):
    serializer_class = TeacherEnrollmentSerializer
    queryset = Enrollment.objects.all()

    def get_queryset(self):
    
        queryset = super().get_queryset()
        section_id = self.kwargs.get('section_id')
        return queryset.filter(Section__id=section_id, type='teacher')