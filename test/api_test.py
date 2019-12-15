import unittest
import requests

class TestAPI(unittest.TestCase):

    def get_url_status(self, url) -> int:
        return requests.get(url).status_code

    def test_get_students(self):
        urls = ["http://localhost:5000/", "http://localhost:5000/students"]
        for url in urls:
            code = self.get_url_status(url)
            self.assertEqual(code, 200, "Consulta fallida")


if __name__ == "__main__":
    unittest.main()