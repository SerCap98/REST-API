from django.utils import timezone

from django.db import models

class BaseEntity(models.Model):
    STATUS_CHOICES = [
        ('EN', 'enabled'),
        ('DS', 'disabled'),
    ]

    id = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='EN',
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.status = 'DS'
        self.deletion_date = timezone.now()
        self.save()
        

class Person(BaseEntity):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200,unique=True)
    
    def delete(self, *args, **kwargs):
        enrollments = Enrollment.objects.filter(Person=self)
        for enrollment in enrollments:
            enrollment.delete()
        super().delete(*args, **kwargs)

class Entity(BaseEntity):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Faculty(Entity):
     pass

class School(Entity):
    Faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)


class Section(Entity):
    SECTION_TYPES = [
        ('MD', 'mandatory'),
        ('EL', 'elective'),
    ]

    uc = models.IntegerField()
    semester = models.IntegerField()
    ht = models.FloatField()
    hp = models.FloatField()
    hl = models.FloatField()
    type = models.CharField(max_length=2, choices=SECTION_TYPES)
    School = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)

class Enrollment(BaseEntity):
    ENROLLMENT_TYPES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=10, choices=ENROLLMENT_TYPES)
    
    class Meta:
        unique_together = ('Person', 'Section',)

