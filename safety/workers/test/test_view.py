from django.test import TestCase
from ..models import Worker

class TestWorkerListView(TestCase):
    def test_view_should_be_accessable(self):
        res = self.client.get('/workers/')
        # print(dir(res))
        self.assertEqual(res.status_code, 200)

    def test_view_should_render_list_of_workser_name(self):
        # GIVEN
        Worker.objects.create(
            first_name='Ball',
            last_name='Kung',
            is_available=True,
            primary_phone='0855555555',
            secondary_phone='0844444444',
            address='Oddsy',
        )
        Worker.objects.create(
            first_name='MuyonZ',
            last_name='Jang',
            is_available=True,
            primary_phone='0655555555',
            secondary_phone='0644444444',
            address='Geeky Base',
        )
        # WHEN
        res = self.client.get('/workers/')
        # THEN
        self.assertContains(res, '<li>Ball</li>')
        self.assertContains(res, '<li>MuyonZ</li>')