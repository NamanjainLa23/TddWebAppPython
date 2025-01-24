#django.tst.TestCase - subclass of python's unittest.Testcase
#sets up test database automatically
from django.test import TestCase

from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """
        uses resolve to map the root URL('/') ti outs corresponding view
        Asserts that the function associated with '/' is home page.
        Ensures that the root URL is correctly routed to the home page view
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        #creates an httprequest to simulate a request to the home page view
        request = HttpRequest()

        #calls the home page request to get the response
        response = home_page(request)

        html = response.content.decode('utf8')

        #validates the home_page view return the correct html structure
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
