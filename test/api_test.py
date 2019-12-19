import unittest
import requests

class TestAPI(unittest.TestCase):

    def get_url_status(self, url) -> int:
        return requests.get(url).status_code

    def test_get_students(self):
        urls = [
            "http://localhost:5000/", 
            "http://localhost:5000/students",
            "http://localhost:5000/students/",
            "http://localhost:5000/students/123asd",
            "http://localhost:5000/students/19111000"
        ]
        codes = [200, 200, 200, 400, 404]
        for index, url in enumerate(urls):
            code = self.get_url_status(url)
            self.assertEqual(code, codes[index], "Consulta fallida")


if __name__ == "__main__":
    unittest.main()