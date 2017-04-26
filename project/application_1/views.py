"""
API view For Document like post, get method for any document.
"""
import logging
from rest_framework.response import Response
from rest_framework.views import APIView

LOGGER = logging.getLogger("application_logs")


class PingView(APIView):
    """
    Get api created to test response time
    This is a test api.
    To test the response time.
    It will just return status 200
    """

    @staticmethod
    def get(request):
        """
        Get API created for Response time check.
        :param request:
        :return: 200 status
        """
        return Response("", status=200)
