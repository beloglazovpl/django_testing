from rest_framework import serializers, exceptions
from django.conf import settings

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if len(value) > settings.MAX_STUDENTS_PER_COURSE:
            raise exceptions.ValidationError(
                f'Превышено максимальное число студентов на курсе: {settings.MAX_STUDENTS_PER_COURSE}'
            )
        return value