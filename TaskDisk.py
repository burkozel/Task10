import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        TOKEN = "AgAAAAATWA31AADLW6_5f7aRAUEMhsvhSK1ALpw"
        HEADERS = {"Authorization": f"OAuth{TOKEN}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", params={"path": file_path}, headers=HEADERS)
        ans = response.json().get("href")
        response_upload = requests.put(ans, files={"file": open(file_path, "rb")}, headers=HEADERS)
        return print(response_upload.status_code, response_upload.text)

if __name__ == '__main__':
    uploader = YaUploader('AgAAAAATWA31AADLW6_5f7aRAUEMhsvhSK1ALpw')
    result = uploader.upload('C:\\Users\\Spectre\\Desktop\\netology9\\file_path\\text.txt')