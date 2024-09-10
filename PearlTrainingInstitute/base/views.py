from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def home(request):
    data = {"message": "Welcome to Pearl Training Institute"}
    return Response(data)
