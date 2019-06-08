from django.test import TestCase

from api.models import Student


class TestStudentModel(TestCase):
    def setUp(self):
        self.regis = Student(student_nim = '16517020', student_name = 'Blablabla', student_nickname = 'Bla', student_gender = True, student_birthplace = 'disini', student_birthdate = '11/12/2013', student_email = 'oksitafly@gmail.com', student_line='lalala', student_mobile='08115128170' )
        self.regis.save()

    def test_student_creation(self):
        self.assertEqual(Student.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.regis.student_name, str(self.regis))