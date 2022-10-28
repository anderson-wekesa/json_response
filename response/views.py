from rest_framework import generics
from .models import Me
from .serializers import MeSerializer

# Create your views here.
class AboutMe(generics.ListCreateAPIView):
    queryset = Me.objects.all()
    serializer_class = MeSerializer