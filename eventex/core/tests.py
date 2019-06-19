from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):

    def setUp(self):
        self.responce = self.client.get("/")

    def test_get(self):
        """GET  / must return status code 200"""
        self.assertEqual(200, self.responce.status_code)


    def test_template(self):
        """ Must use index.html"""
        self.assertTemplateUsed(self.responce, 'index.html')
