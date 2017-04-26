import os

from rest_framework import status
from rest_framework.test import APITestCase


class TestPingCheck(APITestCase):
    """
    Testcase for get operation. Hit ping api and check if sie is up
    """
    def setUp(self):
        self.url_ping = '/application_1/ping/'
        create_log_file()

    def test_ping_get(self):
        """
        Test if Ping Api works
        """
        response = self.client.get(self.url_ping)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        remove_test_log_file()
