from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Details
from .serializers import DetailsSerializer

class DetailsMarks(APIView):
    def get(self, request, Book, Author):
        try:
            details = Details.objects.get(Book=Book, Author=Author)
            serializer = DetailsSerializer(details)
            return Response(serializer.data)
        except Details.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)