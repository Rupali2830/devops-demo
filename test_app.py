import unittest
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen

from app import Handler


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 8081), Handler)
        cls.thread = Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_home_page(self):
        response = urlopen("http://127.0.0.1:8081")
        content = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("Hello from my DevOps application", content)


if __name__ == "__main__":
    unittest.main()