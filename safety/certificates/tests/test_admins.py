from django.contrib import admin
from django.test import TestCase

from ..admin import CertificateAdmin
from ..models import Certificate


class TestWorkerAdmin(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Certificate], CertificateAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'issued_by',
        )
        self.assertEqual(CertificateAdmin.list_display, expected)
