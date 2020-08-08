from rest_framework.viewsets import ModelViewSet

from .models import Certificate
from .serializers import CertificateModelSerializer


class CertificateModeViewSetView(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateModelSerializer
