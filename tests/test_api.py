import os
import sys
import unittest
import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))


class TestAPICases(unittest.TestCase):

    # executed at the beginning of the test
    def setUp(self):
        with app.create_app().app_context():
            self.db_uri = 'sqlite:///' + os.path.join(basedir, 'test.db')
            application = app.create_app()
            application.config['Testing'] = True
            application.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
            self.app = application.test_client()
            self.base_url = '/genes'
            self.params = {"lookup": "BRC"}
            self.invalid_params = {"lookup": "BR"}

    # executed at the end of the test
    def tearDown(self):
        pass

    # Test cases
    def test_api_with_no_input(self):
        print("\n===> Testing the genes endpoint with no input")
        response = self.app.get(self.base_url)
        self.assertEqual(response.status_code, 422)

    def test_api_with_two_char_in_lookup(self):
        print("\n===> Testing the genes endpoint with two character in lookup")
        response = self.app.get(self.base_url, query_string=self.invalid_params)
        self.assertEqual(response.status_code, 422)

    def test_post_method(self):
        print("\n===> Testing the genes endpoint in POST method")
        response = self.app.post(self.base_url)
        self.assertEqual(response.status_code, 405)

    def test_get_method(self):
        print("\n===> Testing the genes endpoint in GET method with lookup parameter")
        response = self.app.get(self.base_url, query_string=self.params)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
