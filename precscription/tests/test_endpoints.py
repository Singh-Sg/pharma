
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.test import Client
from user.models import User
from django.contrib.auth import authenticate
from precscription.factories.factories import DoctorFactory, PatientFactory, UserFactory, DrugFactory
from rest_framework import status
from precscription.models import Precscription
from rest_framework.authtoken.models import Token


class TestPrecscription(APITestCase):
    """
    This class includes test cases for precscription happy path.
    """
    client_class = APIClient

    def setUp(self):
        # Setup function used to create temporary record for test cases.

        self.user = UserFactory(email='admin@admin.com',username='admin', password='pass@123')
        Token.objects.create(user=self.user)
        super(TestPrecscription, self).setUp()

        self.doctor = DoctorFactory(user=self.user, registration_number=123123123)
        self.patient = PatientFactory()
        self.drug = DrugFactory(name='covid')
        self.data = {
            "doctor":self.doctor.user_id,
            "patient":self.patient.user_id,
            "drugs":'["covid1","covid2"]'
        }        

        self.precscription_list = []
        # Create multiple  precscription object using loop.
        for _ in range(3):
            precscription = Precscription.objects.create(doctor=self.doctor, patient=self.patient)
            precscription.drug.add(self.drug)
            self.precscription_list.append(precscription)

        self.precscription_list_url = reverse('api:precscription-list')
        self.precscription_detail_url = reverse("api:precscription-detail", args=[self.precscription_list[0].id])

    def test_precscription_create(self):
        """
        Test case for precscription create.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(self.precscription_list_url, self.data, format="json")
        # Check returned response send 201 status.
        assert response.status_code == status.HTTP_201_CREATED
        # Check returned response is public id and exist in database.
        precscription = Precscription.objects.get(id=response.data["id"])
        assert precscription.id == response.data["id"]

    def test_precscription_detail(self):
        """
        Test case for precscription detail.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.get(self.precscription_detail_url)
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == self.precscription_list[0].id

    def test_all_precscription_detail(self):
        """
        Test case for fetch all precscription.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.get(self.precscription_list_url)
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK