from django.shortcuts import reverse

from rest_framework.test import APITestCase

from api.models import Student


class TestNoteApi(APITestCase):
    def setUp(self):
        # create movie
        self.movie = Student(student_nim = '16517020', student_name = 'Blablabla', student_nickname = 'Bla', student_gender = True, student_birthplace = 'disini', student_birthdate = '11/12/2013', student_email = 'oksitafly@gmail.com', student_line='lalala', student_mobile='08115128170' )
        self.movie.save()

    def test_movie_creation(self):
        response = self.client.post(reverse('students'), {
            'student_nim' : '16517025',
            'student_name' : 'Blablabli', 
            'student_nickname' : 'Bli', 
            'student_gender' : True, 
            'student_birthplace' : 'disini',
            'student_birthdate' : '11/12/2013',
            'student_email' : 'oksiiiitafly@gmail.com',
            'student_line' : 'lalala', 
            'student_mobile': '07115128170' 
        })

        # assert new movie was added
        self.assertEqual(Student.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_movies(self):
        response = self.client.get(reverse('students'), format="json")
        self.assertEqual(len(response.data), 1)

    # def test_updating_movie(self):
    #     response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
    #         'student_nim' : '16517025',
    #         'student_name' : 'Blablablu', 
    #         'student_nickname' : 'Blu', 
    #         'student_gender' : True, 
    #         'student_birthplace' : 'disini',
    #         'student_birthdate' : '11/12/2013',
    #         'student_email' : 'oksiiiitafly@gmail.com',
    #         'student_line' : 'lalala', 
    #         'student_mobile': '07115128170'
    #     }, format="json")

    #     # check info returned has the update
    #     self.assertEqual('Blablablu', response.data['student_name'])

    # def test_deleting_movie(self):
    #     response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

    #     self.assertEqual(204, response.status_code)