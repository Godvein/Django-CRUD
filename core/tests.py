from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import ApiListViewCreate, ApiRetrieveUpdateDestroy
# Create your tests here.

class TestUrls(SimpleTestCase):

    #test api class view url
    def test_apilistview_resolve(self):
        url = reverse('apiview')
        self.assertEqual(resolve(url).func.view_class, ApiListViewCreate)