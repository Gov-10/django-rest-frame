from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_home(request):
    body = request.body
    print(body)  #prints byte string of JSON data
    # return JsonResponse({"message" : "hello"})
    data = {}
    json.loads(body)
    return JsonResponse(data)
