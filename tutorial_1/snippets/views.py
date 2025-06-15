from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":  #for reading
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe= False)
    elif request.method == "POST": #for creating
        data = JSONParser().parse(request)
        serial = SnippetSerializer(data= data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status = 400)

@csrf_exempt
def snippet_detail(request, pk):
     """
    Retrieve, update or delete a code snippet.
    """
     try:
         snippet = Snippet.objects.get(pk=pk)
     except Snippet.DoesNotExist:
         return HttpResponse(status=404)
     
     if request.method == "GET":
         serializer = SnippetSerializer(snippet)
         return JsonResponse(serializer.data, safe=False)
     elif request.method=="PUT":
         data = JSONParser().parse(request)
         serial = SnippetSerializer(data=data)
         if serial.is_valid():
             serial.save()
             return JsonResponse(serial.data, status=201)
         return JsonResponse(serial.errors, status= 400)
     elif request.method == "DELETE":
         snippet.delete()
         return HttpResponse(status=200)
      