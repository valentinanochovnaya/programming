from .models import Freelancer
from rest_framework import routers, serializers, viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FreelancerSerializer


class FreelancerViewSet(viewsets.ModelViewSet):
    serializer_class = FreelancerSerializer
    queryset = Freelancer.objects.all()
    lookup_field = "id"
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = "__all__"