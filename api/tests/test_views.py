from django.shortcuts import reverse

from rest_framework.test import APITestCase

from api.models import Student


class TestNoteApi(APITestCase):
    def setUp(self):
        # create Student
        self.student = Student(nim = '16517020', name = 'Blablabla', nickname = 'Bla', gender = True, birth_place = 'disini', birth_date = '11/12/2013', email = 'oksitafly@gmail.com', line='lalala', mobile='08115128170', address_home="disini", address_local="disana", disease="Alergi tugas", blood_type="S+", guardian_name="Sendiri", guardian_rel="Aku", guardian_mobile="0812345678", consent=True)
        self.student.save()

    def test_student_creation(self):
        response = self.client.post(reverse('students'), {
            'nim' : '16517020', 
            'name' : 'Blablabla', 
            'nickname' : 'Bla', 
            'gender' : 0, 
            'birth_place' : 'disini', 
            'birth_date' : '11/12/2013', 
            'email' : 'oksitafly@gmail.com', 
            'line' : 'lalala', 
            'mobile' : '08115128170', 
            'address_home' : "disini", 
            'address_local' : "disana", 
            'disease' : "Alergi tugas", 
            'blood_type' : "S+", 
            'guardian_name' : "Sendiri", 
            'guardian_rel' : "Aku", 
            'guardian_mobile' : "0812345678", 
            'consent' : True
        })

        # assert new movie was added
        self.assertEqual(Student.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_students(self):
        response = self.client.get(reverse('students'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_student(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'nim' : '16517020', 
            'name' : 'Blablablu', 
            'nickname' : 'Bla', 
            'gender' : 0, 
            'birth_place' : 'disini', 
            'birth_date' : '11/12/2013', 
            'email' : 'oksitafly@gmail.com', 
            'line' : 'lalala', 
            'mobile' : '08115128170', 
            'address_home' : "disini", 
            'address_local' : "disana", 
            'disease' : "Alergi tugas", 
            'blood_type' : "S+", 
            'guardian_name' : "Sendiri", 
            'guardian_rel' : "Aku", 
            'guardian_mobile' : "0812345678", 
            'consent' : True
        }, format="json")

        # check info returned has the update
        self.assertEqual('Blablablu', response.data['name'])

    def test_deleting_student(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)