from rest_framework import viewsets
from rest_framework.response import Response
from .models import Precscription, Drug
from .serializers import PrecscriptionSerializer
from user.models import Doctor, Patient
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
import json
from .services.services import CreatePrecscriptionService


class PrecscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows precscriptions to be viewed or edited.
    """
    queryset = Precscription.objects.all()
    serializer_class = PrecscriptionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # creating a precscription.
        try:
            precscription = CreatePrecscriptionService.execute(request.data)
            return Response(precscription, status=status.HTTP_201_CREATED)
        except Doctor.DoesNotExist:
            return Response({"error": 'doctor for id={} not exist.'.format(request.data['doctor'])}, status.HTTP_404_NOT_FOUND)
        except Patient.DoesNotExist:
            return Response({"error": 'patient for id={} not exist.'.format(request.data['patient'])}, status.HTTP_404_NOT_FOUND)