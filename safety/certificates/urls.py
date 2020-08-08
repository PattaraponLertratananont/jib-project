from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CertificateModeViewSetView


router = DefaultRouter()
router.register(r'', CertificateModeViewSetView)

urlpatterns = [
    path('', include(router.urls)),
]
