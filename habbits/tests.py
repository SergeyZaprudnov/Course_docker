from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from habbits.models import Habbit
from users.models import Users


class HabbitTestCase(APITestCase):

    def setUp(self):
        """ Prepare testing """
        self.user = Users(
            email="test@gmail.com",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        self.user.set_password("test")
        self.user.save()

        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_habbit(self):
        """ Test habit creation """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 1
        }

        response = self.client.post("/api/v1/habbit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habbit.objects.all().exists())

    def test_get_share_habbits(self):
        """ Test get info about user public habits """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        data2 = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/api/v1/habbit/create/", data)
        self.client.post("/api/v1/habbit/create/", data2)
        response = self.client.get("/api/v1/share_habbits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_habbits(self):
        """ Test get info about user habits """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        data2 = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/api/v1/habbit/create/", data)
        self.client.post("/api/v1/habbit/create/", data2)
        response = self.client.get("/api/v1/habbits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_full_information_habbit(self):
        """ Test get full information about user habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 2
        }

        self.client.post("/api/v1/habbit/create/", data)
        response = self.client.get("/api/v1/habbit/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habbit(self):
        """ Test updating user habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }
        new_data = {
            "place": "At home.",
            "time": "17:00:00",
            "action": "Do homework.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }

        self.client.post("/api/v1/habbit/create/", data)
        response = self.client.put("/api/v1/habbit/update/3/", new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_duration_create_habbit(self):
        """ Test that user con not create habit with duration greater than 120 seconds """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 200,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/api/v1/habbit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_pleasant_create_habbit(self):
        """ Test that pleasant habit does not have award """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "True",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/api/v1/habbit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_usual_create_habbit(self):
        """ Test that usual habit must has award or pleasant habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "duration": 10,
            "is_public": "True",
            "owner": 5
        }

        response = self.client.post("/api/v1/habbit/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
