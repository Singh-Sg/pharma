from rest_framework import serializers
from .models import Doctor, Patient
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model which use to convert queryset into json format.
    """
    class Meta:
        model = User
        fields = ('username')


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for Doctor model which use to convert queryset into json format.
    """
    name = serializers.CharField(source='user.username')
    address = serializers.CharField(source='user.address_part1')

    class Meta:
        model = Doctor
        fields = ("name", 'address', 'qualification', 'registration_number')

    # TODO
    # def to_representation(self, instance):
    #     rep = super(DoctorSerializer, self).to_representation(instance)
    #     rep['name'] = instance.user.username
    #     rep['address'] = instance.user.address_part1
    #     rep['qualification'] = instance.qualification
    #     rep['registration_number'] = instance.registration_number

    #     return rep


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for Patient model which use to convert queryset into json format.
    """
    name = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    phone = serializers.CharField(source='user.phone_number')
    birthday = serializers.CharField(source='user.birthday')
    age = serializers.CharField(source='user.age')
    address = serializers.CharField(source='user.address_part1')

    class Meta:
        model = Patient
        fields = ('name', "email", 'age', 'birthday', "phone", 'address', 'date_of_consultant')
