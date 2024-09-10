from rest_framework import generics
from .models import Admission
from .serializers import AdmissionSerializer


class AdmissionListCreateView(generics.ListCreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
