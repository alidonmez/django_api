from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FormEntry
from .serializers import FormEntrySerializer
from datetime import datetime

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_forms(request, pk):
    try:
        form = FormEntry.objects.get(pk=pk)
    except FormEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FormEntrySerializer(form)
        return Response(serializer.data)
    
    # delete a single FormEntry
    elif request.method == 'DELETE':
        return Response({})
    
    # update details of a single FormEntry
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_forms(request):
    if request.method == 'GET':
        forms = FormEntry.objects.all()
        serializer = FormEntrySerializer(forms, many=True)
        return Response(serializer.data)
    # insert a new record for a FormEntry
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'dob': request.data.get('dob'),
            'notes': request.data.get('notes'),
        }
        serializer = FormEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)