from rest_framework import generics
from classes.models import Classes
from .serializers import ClassesSerializer
#f  rom rest_framework import IsAuthenticated

class ClassesListCreateView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    #permission_classes = [IsAuthenticated]

class ClassesUpdateDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    #permission_classes = [IsAuthenticated]