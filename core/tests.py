from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import ApiListViewCreate
# Create your tests here.

class TestUrls(SimpleTestCase):

    #test api class view url
    def test_apilistview_resolve(self):
        url = reverse('apiview')
        self.assertEqual(resolve(url).func.view_class, ApiListViewCreate)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("insert")
    def test_insert(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    
