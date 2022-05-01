from django.shortcuts import render
import requests

# Create your views here.
def get_music(request):
    return render(request, 'music/music.html')