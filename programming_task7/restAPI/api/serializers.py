from rest_framework import serializers
from api.models import Freelancer


class FreelancerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Freelancer
        fields = ('id',
                  'name',
                  'email',
                  'phone_number',
                  'availability',
                  'salary',
                  'position')