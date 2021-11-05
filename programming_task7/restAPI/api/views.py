from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import Freelancer
from api.serializers import FreelancerSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def freelancers_list(request):
    if request.method == 'GET':
        freelancers = Freelancer.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            freelancers = freelancers.filter(title__icontains=name)
        freelancers_serializer = FreelancerSerializer(freelancers, many=True)
        return JsonResponse(freelancers_serializer.data, safe=False)
    elif request.method == 'POST':
        freelancer_data = JSONParser().parse(request)
        freelancers_serializer = FreelancerSerializer(data=freelancer_data)
        if freelancers_serializer.is_valid():
            freelancers_serializer.save()
            return JsonResponse(freelancers_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(freelancers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Freelancer.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def freelancer_detail(request, pk):
    try:
        freelancer = Freelancer.objects.get(pk=pk)
        if request.method == 'GET':
            freelancers_serializer = FreelancerSerializer(freelancer)
            return JsonResponse(freelancers_serializer.data)
        elif request.method == 'PUT':
            freelancer_data = JSONParser().parse(request)
            freelancers_serializer = FreelancerSerializer(freelancer, data=freelancer_data)
            if freelancers_serializer.is_valid():
                freelancers_serializer.save()
                return JsonResponse(freelancers_serializer.data)
            return JsonResponse(freelancers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            freelancer.delete()
            return JsonResponse({'message': 'Freelancer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return JsonResponse({'message': 'The freelancer does not exist'}, status=status.HTTP_404_NOT_FOUND)
