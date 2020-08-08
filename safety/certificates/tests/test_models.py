from django.test import TestCase

from ..models import Certificate


class TestCertificate(TestCase):
    def test_certificate_should_have_defined_field(self):
        # Given
        name = 'Django Certificat by Odds'
        issued_by = 'ProoF'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
        )
        # Then
        assert certificate.name == name
        assert certificate.issued_by == issued_by
