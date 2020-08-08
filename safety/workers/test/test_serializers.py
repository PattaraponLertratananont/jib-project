from django.test import TestCase
from ..models import Worker
from ..serializers import WorkerSerializer


class TestWorkerSerializer(TestCase):
    def test_serializer_should_return_correct_serialized_data(self):
        worker = Worker.objects.create(
            first_name='Ball',
            last_name='Kung',
            is_available=True,
            primary_phone='0855555555',
            secondary_phone='0844444444',
            address='Odds Tria',
        )
        serializer = WorkerSerializer(worker)
        expected = {
            'first_name': 'Ball',
            'last_name': 'Kung',
            'is_available': True,
            'primary_phone': '0855555555',
            'secondary_phone': '0844444444',
            'address': 'Odds Tria',
        }
        assert serializer.data == expected
