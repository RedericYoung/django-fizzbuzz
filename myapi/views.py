from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fizz
from .serializers import FizzSerializer
import uuid

class FizzBuzzList(APIView):
    permission_classes = []

    def get(self, request):
        serializer = FizzSerializer(Fizz.objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'sport': request.data.get('sport'), 
            'completed': request.data.get('completed'),
            'id': uuid.uuid1()
        }

        serializer = FizzSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def detail(self, id):
    data = Fizz.objects.filter(id = id)
    serializer = FizzSerializer(data, many=True)

    if(data.first()):
        return JsonResponse(serializer.data[0], status=status.HTTP_200_OK, safe=False)

    return JsonResponse({'Error': 'Record not Found'}, status=status.HTTP_400_BAD_REQUEST, safe=False)

