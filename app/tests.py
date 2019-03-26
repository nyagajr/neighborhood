from django.test import TestCase
from .models import *



# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.junior=Hood(hood_name='hooh',hood_photo = 'junior.jpg', location = 'usa',link_hood = 'mee', occupant_count = '100')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.junior,Hood))
