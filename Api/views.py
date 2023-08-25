from django.shortcuts import render
from .models import BookModel
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def Get_view(request):
    books = BookModel.objects.all()
    serializer = BookSerializer(books,many = True)

    return Response(serializer.data)

