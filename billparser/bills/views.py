from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User,Bills
from .serializers import billSerializer
# Create your views here.


class EndUser(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Bills.objects.all()
        serializer = billSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
         serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))
                       
#     def retrieve(self, request, pk=None):
#         pass

   
class InternalUser(viewsets.ModelViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = billSerializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass