from django.test import TestCase

from api.models import Student


class TestStudentModel(TestCase):
    def setUp(self):
        self.regis = Student(nim = '16517020', name = 'Blablabla', nickname = 'Bla', gender = 0, birth_place = 'disini', birth_date = '11/12/2013', email = 'oksitafly@gmail.com', line='lalala', mobile='08115128170', address_home="disini", address_local="disana", disease="Alergi tugas", blood_type="S+", guardian_name="Sendiri", guardian_rel="Aku", guardian_mobile="0812345678", consent=True)
        self.regis.save()

    def test_creation(self):
        self.assertEqual(Student.objects.count(), 1)

    def test_representation(self):
        self.assertEqual(self.regis.name, str(self.regis))