from service_objects.services import Service
from user.models import Doctor, Patient
from precscription.models import Precscription, Drug
import json
from precscription.serializers import PrecscriptionSerializer


class CreatePrecscriptionService(Service):
    """
    Extending Service from service objects to write logic for creating Precscription.
    """

    def process(self):
        for drug in json.loads(self.data.get('drugs')):
            Drug.objects.get_or_create(name=drug)
        drug = Drug.objects.filter(name__in=json.loads(self.data.get('drugs')))
        if drug:
            precscription = Precscription(doctor_id=self.data.get('doctor'), patient_id=self.data.get('patient'))
            precscription.save()
            precscription.drug.add(*drug)
            serializer = PrecscriptionSerializer(precscription)
        # TODO
        else:
            # will add a logic for drugs if not present in drugs model.
            pass
        return serializer.data