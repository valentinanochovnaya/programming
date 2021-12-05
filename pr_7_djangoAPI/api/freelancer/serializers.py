from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Freelancer


class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = '__all__'
        # fields = ( 'name', 'email', 'phone_number', 'availability', 'salary', 'position')
        read_only_fields = ('id',)
