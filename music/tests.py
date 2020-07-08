from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer


class BaseViewTest(APITestCase):
    client = APIClient

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        self.create_song("Can't Fight", "Lianne La Havas")
        self.create_song("True Faith", "Lotte Kestner")
        self.create_song("Making My Way", "Jack Broadbent")
        self.create_song("through the valley", "Shawn James")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )

        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
