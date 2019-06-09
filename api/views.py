from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.models import Student
from api.serializers import StudentSerializer


class StudentCreateView(CreateAPIView):
    """
    Undetailed view for creation
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListView(ListCreateAPIView):
    """
    Undetailed view for Listing
    """
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    """
    Detailed view for edit&delete
    """
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer