import json

from adchieveProject.distances.api.views import Distance
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

factory = APIRequestFactory()


class DistanceTestCase(APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.valid_payload = [
            {
                "name": "Eastern Enterprise B.V.",
                "address": "Deldenerstraat 70, 7551AH Hengelo, The Netherlands"
            },
            {
                "name": "Eastern Enterprise",
                "address": "46/1 Office no 1 Ground Floor , Dada House , Inside dada silk mills compound, Udhana Main Rd, near Chhaydo Hospital, Surat, 394210, India"
            },
            {
                "name": "Adchieve Rotterdam",
                "address": "Weena 505, 3013 AL Rotterdam, The Netherlands"
            },
            {
                "name": "Sherlock Holmes",
                "address": "221B Baker St., London, United Kingdom"
            },
            {
                "name": "The White House",
                "address": "1600 Pennsylvania Avenue, Washington, D.C., USA"
            },
            {
                "name": "The Empire State Building",
                "address": "350 Fifth Avenue, New York City, NY 10118"
            },
            {
                "name": "The Pope",
                "address": "Saint Martha House, 00120 Citta del Vaticano, Vatican City"
            },
            {
                "name": "Neverland",
                "address": "5225 Figueroa Mountain Road, Los Olivos, Calif. 93441, USA"
            }
        ]
        self.invalid_payload = []

    def test_create_csv(self):
        """Test the api has bucket creation capability."""
        api_request = factory.post(
            '',
            data=json.dumps(self.valid_payload, default=str),
            content_type='application/json'
        )
        detail_view = Distance.as_view(actions={'post': 'create'})
        response = detail_view(api_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_csv(self):
        api_request = factory.post(
            '',
            data=json.dumps(self.valid_payload, default=str),
            content_type='application/json'
        )
        detail_view = Distance.as_view(actions={'post': 'create'})
        response = detail_view(api_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
