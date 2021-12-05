from django.shortcuts import render
from .serializers import FreelancerSerializer
from .models import Freelancer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .swagger_docs import EndpointDocs
from drf_yasg.utils import swagger_auto_schema


class FreelancerAPIView(ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
    http_method_names = ["get", "post"]

    @swagger_auto_schema(**EndpointDocs.POST)
    def post(self, request):
        serializer = FreelancerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200,
                             "message": "Freelancer successfully created",
                             "certificate": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificFreelancerAPIView(APIView):

    def get_object(self, identifier):
        try:
            return Freelancer.objects.get(id=identifier)
        except Freelancer.DoesNotExist:
            return Response({"status": 404,
                             "message": "Freelancer not found"},
                            status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**EndpointDocs.GET)
    def get(self, request, identifier):
        freelancer = self.get_object(identifier)
        if isinstance(freelancer, Response):
            return freelancer

        serializer = FreelancerSerializer(freelancer)
        return Response(serializer.data)

    @swagger_auto_schema(**EndpointDocs.PUT)
    def put(self, request, identifier):
        freelancer = self.get_object(identifier)
        if isinstance(freelancer, Response):
            return freelancer

        freelancer_data = JSONParser().parse(request)
        serializer = FreelancerSerializer(freelancer, data=freelancer_data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200,
                             "message": "Freelancer successfully updated",
                             "freelancer": serializer.data},
                            status=status.HTTP_200_OK)

        return Response({"status": 400,
                         "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**EndpointDocs.DELETE)
    def delete(self, request, identifier):
        freelancer = self.get_object(identifier)
        if isinstance(freelancer, Response):
            return freelancer

        freelancer.delete()
        return Response({"status": 200,
                         "message": "Successfully deleted!"},
                        status=status.HTTP_200_OK)

