from rest_framework.response import Response
from rest_framework.views import APIView
from ..utils.calculation_utils import get_distances


class Distance(APIView):
    def post(self, request):
        address_details = request.data
        get_distances(address_details)
        return Response('Done')
