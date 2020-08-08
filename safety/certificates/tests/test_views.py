from django.test import TestCase

from ..models import Certificate
from ..serializers import CertificateModelSerializer
from ..views import CertificateModeViewSetView


class TestCertificateListView(TestCase):
    def test_view_should_be_accessable(self):
        res = self.client.get('/certificates/')
        assert res.status_code == 200

    def test_model_view_set_should_set_queryset(self):
        assert list(CertificateModeViewSetView.queryset) == list(Certificate.objects.all())

    def test_model_view_set_should_set_serializer_class(self):
        assert CertificateModeViewSetView.serializer_class == CertificateModelSerializer
