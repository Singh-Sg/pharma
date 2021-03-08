from rest_framework import serializers
from .models import Precscription, Drug
from user.serializers import DoctorSerializer, PatientSerializer


class DrugSerializer(serializers.ModelSerializer):
    """
    Serializer for Drug model which use to convert queryset into json format.
    """
    class Meta:
        model = Drug
        fields = ('name',)

    def to_representation(self, instance):
        # Use to update the representation of value for fields.
        rep = super(DrugSerializer, self).to_representation(instance)
        rep['strength'] = '{} {}'.format(instance.strength, instance.get_strength_unit_display())
        rep['durations'] = '{} {}'.format(instance.durations, instance.get_duration_unit_display()) 
        rep['dose'] = '{} {}'.format(instance.dose, instance.get_dose_unit_display())
        rep['preparation'] = '{}'.format(instance.get_preparation_display())
        rep['frequency'] = '{}'.format(instance.get_frequency_display())
        rep['route'] = '{}'.format(instance.get_route_display())
        return rep


class PrecscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for Precscription model which use to convert queryset into json format.
    """
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    drug = DrugSerializer(read_only=True, many=True)

    class Meta:
        model = Precscription
        fields = '__all__'
