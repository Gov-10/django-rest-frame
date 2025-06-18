from django.shortcuts import render
from .serializers import AdvocateSerializer
from .models import Advocate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
# Create your views here.
@api_view(['GET', 'POST'])
def advocate_list(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query is None:
            query = ''
        lis = Advocate.objects.filter( Q(username__icontains = query) | Q(bio__icontains = query))
        serial = AdvocateSerializer(lis, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        ser = AdvocateSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    try:
        adv = Advocate.objects.get(username= username)
    except Advocate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serial = AdvocateSerializer(adv)
        return Response(serial.data, status=status.HTTP_200_OK)
    elif request.method =="PUT":
        data = request.data
        ser = AdvocateSerializer(instance = adv, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        adv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    


    
    