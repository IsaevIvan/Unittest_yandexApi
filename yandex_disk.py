import requests

class YandexDiskApi:

    def __init__(self, token):
        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {"Authorization": f'{self.token}'}

    def create_folder(self, path):
        url = self.base_url
        params = {"path": path}
        response = requests.put(url, headers=self.headers, params=params)
        return response

    def folder_exists(self, path):
        url = self.base_url
        params = {"path": path}
        response = requests.get(url, headers=self.headers, params=params)
        return response.status_code == 200

    def delete_folder(self, path, permanently=True):
        url = self.base_url
        params = {"path": path,
                  "permanently": str(permanently).lower()}
        response = requests.delete(url, headers=self.headers, params=params)
        return response.status_code


