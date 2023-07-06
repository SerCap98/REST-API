from rest_framework import serializers
from .models import *

class BaseEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseEntity
        read_only_fields = ['created_at', 'deleted_at']

class PersonSerializer(BaseEntitySerializer):
    class Meta(BaseEntitySerializer.Meta):
        model = Person
        fields = '__all__'

class FacultySerializer(BaseEntitySerializer):
    class Meta(BaseEntitySerializer.Meta):
        model = Faculty
        fields = '__all__'

class SchoolSerializer(BaseEntitySerializer):
    class Meta(BaseEntitySerializer.Meta):
        model = School
        fields = '__all__'

class SectionSerializer(BaseEntitySerializer):
    class Meta(BaseEntitySerializer.Meta):
        model = Section
        fields = '__all__'

class EnrollmentSerializer(BaseEntitySerializer):
    class Meta(BaseEntitySerializer.Meta):
        model = Enrollment
        fields = '__all__'

class StudentEnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['student']

    def get_student(self, obj):
        if obj.type == 'student':
            return PersonSerializer(obj.Person).data
        return None

class TeacherEnrollmentSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['teacher']

    def get_teacher(self, obj):
        if obj.type == 'teacher':
            return PersonSerializer(obj.Person).data
        return None
