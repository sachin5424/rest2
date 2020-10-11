from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category,Vlog
from .serializers import Categoryserializers,Vlogserializers
# Create your views her
@api_view(['GET', 'POST'])
def vlog_list(request,format=None):
    """
    List all code Vlogs, or create a new Vlog.
    """
    if request.method == 'GET':
        snippets = Vlog.objects.all()
        serializer = Vlogserializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Vlogserializers(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Vlog.objects.get(pk=pk)
    except Vlog.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = Vlogserializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = Response().parse(request)
        serializer = Vlogserializers(snippet, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)