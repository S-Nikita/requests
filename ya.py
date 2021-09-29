import requests
from requests.models import Response


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_href_for_upload(self, upload_path):
        headers = self.get_headers()
        params = {"path": upload_path, "overwrite": "true"}
        url = f'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            print('Success')
        return response.json()['href']

    def upload(self, file_path: str):
        href = self._get_href_for_upload(file_path)
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.put(url=href, headers=headers, params=params)

        if response.status_code == 201:
            return 'Файл был успешно загружен'
        else:
            return 'Ошибка при выполнении запроса'
