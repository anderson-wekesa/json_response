from rest_framework import generics
from .models import Me
from .serializers import MeSerializer

# Create your views here.
#@api_view(['GET'])
class AboutMe(generics.ListCreateAPIView):
    queryset = Me.objects.all()
    serializer_class = MeSerializer
    http_method_names = ['get', 'options']
