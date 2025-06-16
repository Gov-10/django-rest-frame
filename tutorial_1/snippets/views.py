# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from .models import Snippet
# from .serializers import SnippetSerializer

# # Create your views here.
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":  #for reading
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe= False)
#     elif request.method == "POST": #for creating
#         data = JSONParser().parse(request)
#         serial = SnippetSerializer(data= data)
#         if serial.is_valid():
#             serial.save()
#             return JsonResponse(serial.data, status=201)
#         return JsonResponse(serial.errors, status = 400)

# @csrf_exempt
# def snippet_detail(request, pk):
#      """
#     Retrieve, update or delete a code snippet.
#     """
#      try:
#          snippet = Snippet.objects.get(pk=pk)
#      except Snippet.DoesNotExist:
#          return HttpResponse(status=404)
     
#      if request.method == "GET":
#          serializer = SnippetSerializer(snippet)
#          return JsonResponse(serializer.data, safe=False)
#      elif request.method=="PUT":
#          data = JSONParser().parse(request)
#          serial = SnippetSerializer(data=data)
#          if serial.is_valid():
#              serial.save()
#              return JsonResponse(serial.data, status=201)
#          return JsonResponse(serial.errors, status= 400)
#      elif request.method == "DELETE":
#          snippet.delete()
#          return HttpResponse(status=200)
      
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Snippet
# from .serializers import SnippetSerializer
# from rest_framework.parsers import JSONParser
# from rest_framework import status

# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serial = SnippetSerializer(data = data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data, status=status.HTTP_201_CREATED)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serial = SnippetSerializer(data= data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data, status=status.HTTP_201_CREATED)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# from .models import Snippet
# from .serializers import SnippetSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser
# from rest_framework import status

# def snippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request, format = None):
#         data = JSONParser().parse(request)
#         serial = SnippetSerializer(data=data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data, status= status.HTTP_201_CREATED)
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# def snippetDetail(APIView):
#     def get_obj(self, request, pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#             return snippet
#         except Snippet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request,pk, format= None):
#         serializer = SnippetSerializer(self.get_obj(pk))
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request,pk, format= None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request,pk, format= None):
#         snippet = get_obj(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class  = SnippetSerializer