from datetime import datetime, timedelta
from factory import SubFactory, django, fuzzy
from user.models import Doctor, Patient, User
from precscription.models import Drug, Precscription

#Creating  dummy models.


class UserFactory(django.DjangoModelFactory):
    """
    Factory-boy for User model
    """

    class Meta:
        model = User


class DoctorFactory(django.DjangoModelFactory):
    """
    Factory-boy for Doctor model
    """
    user = SubFactory(UserFactory)

    class Meta:
        model = Doctor


class PatientFactory(django.DjangoModelFactory):
    """
    Factory-boy for Patient model
    """
    user = SubFactory(UserFactory)
    
    class Meta:
        model = Patient


class DrugFactory(django.DjangoModelFactory):
    """
    Factory-boy for drug model
    """

    class Meta:
        model = Drug


class PrecscriptionFactory(django.DjangoModelFactory):
    """
    Factory-boy for precscription model
    """
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(PatientFactory)
    drug = SubFactory(DrugFactory)

    class Meta:
        model = Precscription
