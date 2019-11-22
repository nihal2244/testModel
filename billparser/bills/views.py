from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import User,Bills
from .serializers import billSerializer
# Create your views here.


class EndUser(viewsets.ViewSet):
    def list(self, request):
        queryset = Bills.objects.all()
        serializer = billSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
         serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))
                       
#     def retrieve(self, request, pk=None):
#         pass

   
class InternalUser(viewsets.ViewSet):
    def list(self, request):
        queryset = Bills.objects.all()
        serializer = billSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        file_serializer = billSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Bills.objects.all()
        bills = get_object_or_404(queryset, pk=pk)
        serializer = billSerializer(bills)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Bills.objects.all()
        print(queryset)
        serializer = billSerializer(instance=queryset,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        serializer = billSerializer(request.user, data=request.data, partial=True)
        serializer.save()
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     pass