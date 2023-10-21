from django.test import TestCase

class PersonTestCase(TestCase):

    def testSmoke(self):
        self.assertEqual("smoke", "smoke")
