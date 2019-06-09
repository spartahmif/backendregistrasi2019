from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_nim', 'student_name', 'student_nickname', 'student_gender', 'student_birthplace', 'student_birthdate', 'student_email', 'student_line', 'student_mobile')
        extra_kwargs = {
            'id': {'read_only': True}
        }