from django.test import TestCase
from django.urls import reverse


class StartPageTests(TestCase):
    
    start_page_url = '/'

    def test_page_loads(self):
        response = self.client.get(self.start_page_url)
        self.assertEqual(response.status_code, 200) # type: ignore

    def test_page_contains_todoist_url(self):
        response = self.client.get(self.start_page_url)
        self.assertContains(response, reverse('todoist'))


