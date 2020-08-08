from django.test import TestCase

from ..models import Certificate
from workers.models import Worker


class TestCertificate(TestCase):
    def test_certificate_should_have_defined_field(self):
        # Given
        worker = Worker.objects.create(
            first_name='Ball',
            last_name='Kung',
            is_available=True,
            primary_phone='0855555555',
            secondary_phone='0844444444',
            address='Oddsy',
        )
        name = 'Django Certificate by Odds'
        issued_by = 'ProoF'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
            worker=worker,
        )
        # Then
        assert certificate.name == name
        assert certificate.issued_by == issued_by
        assert certificate.worker.first_name == worker.first_name
