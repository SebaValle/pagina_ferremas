from django.shortcuts import render

<<<<<<< HEAD
=======
# Create your views here.
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
from rest_framework import viewsets
from .models import Cliente
from .serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer