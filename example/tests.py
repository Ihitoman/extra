from django.test import TestCase
from example.models import Cosa

class CosaTest(TestCase):
    def setUp(self):
        Cosa.objects.Create(name = "prueba", actividad_id=1)

    def test_post(self):
        cosa1 = Cosa.objects.get(pk=4)
        self.assertEqual(cosa1.name, 'prueba')
# Create your tests here.
