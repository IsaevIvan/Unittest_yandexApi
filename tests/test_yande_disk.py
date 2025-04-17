import unittest
import os
from dotenv import load_dotenv
from yandex_disk import YandexDiskApi


class TestYandexDiskApi(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.token = os.getenv('YANDEX_DISK_TOKEN')
        self.disk = YandexDiskApi(self.token)
        self.test_folder_name = "test_folder_for_api"
        self.test_folder_path = f"/{self.test_folder_name}"

    def tearDown(self):
        try:
            self.disk.delete_folder(self.test_folder_path)
        except:
            pass

    def test_create_folder_success(self):
        response = self.disk.create_folder(self.test_folder_path)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.disk.folder_exists(self.test_folder_path))

    def test_create_folder_already_exists(self):
        self.disk.create_folder(self.test_folder_path)
        response = self.disk.create_folder(self.test_folder_path)
        self.assertEqual(response.status_code, 409)

    def test_create_folder_unauthorized(self):
        disk = YandexDiskApi("invalid_token")
        response = disk.create_folder(self.test_folder_path)
        self.assertEqual(response.status_code, 401)

    def test_create_folder_invalid_path(self):
        response = self.disk.create_folder("//invalid/path")
        self.assertEqual(response.status_code, 404)

    def test_create_folder_no_token(self):
        disk = YandexDiskApi(None)
        disk.headers = {}
        response = disk.create_folder(self.test_folder_path)
        self.assertEqual(response.status_code, 401)
