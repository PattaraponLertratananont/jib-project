import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Worker


class TestWorker(TestCase):
    def test_worker_should_have_defined_field(self):
        # Given
        first_name = 'Keng'
        last_name = 'Mak'
        is_available = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-689-778x'
        address = 'Geeke Base All Star'

        # Mock image for TestImage
        image_mock = MagicMock(spec=File)
        image_mock.name = 'ball.png'
        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            image_profile=image_mock,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )
        # Then
        # self.assertEqual(worker.first_name, first_name)
        assert worker.first_name == first_name
        self.assertEqual(worker.last_name, last_name)
        # self.assertTrue(worker.is_available, is_available)
        assert worker.is_available is True
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)
        self.assertEqual(worker.image_profile, image_mock.name)

        os.remove('media/' + image_mock.name)

    def test_model_should_have_friendly_name(self):
        first_name = 'Ball'
        last_name = 'Kung'
        is_available = True
        primary_phone = '0855555555'
        secondary_phone = '0844444444'
        address = 'Geeke Base All Star'

        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )
        assert worker.__str__() == f'{first_name} {last_name}'
