from rest_framework.response import Response
from rest_framework.views import APIView
from ..utils.calculation_utils import get_distances


class Distance(APIView):
    def post(self, request):
        address_details = request.data
        if request.data:
            response = get_distances(address_details)
            return Response(response, status=201)

        else:
            response = {'message': 'Invalid input'}
            return Response(response, status=400)
