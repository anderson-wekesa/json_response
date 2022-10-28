#from rest_framework import generics
#from .models import Me
#from .serializers import MeSerializer

#from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
class AboutMe():
    http_method_names = ['get', 'options']

    def home(request, *args, **kwargs):
      header = {"Access-Control-Allow-Origin":"*"}
      data = {
        "slackUsername":"callmeanderson",
        "backend":True,
        "age": 21,
        "bio":"Django developer with a few months experience. I am a tech enthusiast and a rock lover."
      }
      return JsonResponse(data, headers=header)
