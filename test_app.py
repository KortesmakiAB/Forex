from unittest import TestCase
from app import app
from functions import *

class ForexTests(TestCase):
    """
    Test Flask Routes
    """

    def setUp(self):
        """Before each test...
        Make Flask errors be real errors, not HTML pages with error info.
        Stop flask debug toolbar from running and interfering with tests (This is a bit of a hack)"""

        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


    def test_index_and_base_html(self):
        """Test for status code. Test for html in base.html and index.html"""

        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<input type="text" class="form-control" id="converting-from" name="from" required>', html)
            self.assertIn('<title>Currency Converter</title>', html)


    def test_conversion(self):
        """Test for successful currency conversion US $100 to "US$ 100.00". Test for html in conversion.html"""

        with app.test_client() as client:
            resp = client.get('/conversion?from=USD&to=USD&amt=100')
            html = resp.get_data(as_text=True)

            self.assertIn('converts to US$ 100.00', html)
            self.assertIn('<form action="/">', html)
            self.assertEqual(resp.status_code, 200)

    
    def test_redirect(self):
        """Feed invalid "from" parameter to test for redirect response"""

        with app.test_client() as client:
            resp = client.get('/conversion?from=SPRINGBOARD&to=JPY&amt=1')

            self.assertEqual(resp.status_code, 302)


    def test_error_message(self):
        """Feed invalid "to" parameter to test for redirect followed AND test for proper error message."""

        with app.test_client() as client:
            resp = client.get('/conversion?from=USD&to=SPRINGBOARD&amt=20', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertIn('<p>Please enter a valid', html)
            self.assertIn('Converting to:', html)
            self.assertEqual(resp.status_code, 200)