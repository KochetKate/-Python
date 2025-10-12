import requests


class YouGile:
    def __init__(self, url, login=None, password=None, companyId=None):
        self.url = url
        self.token = self.get_token(login, password, companyId)

    def get_token(self, login, password, companyId):
        # Получение токена
        payload = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)
        response_data = resp.json()
        return response_data[0]['key']

    def get_projects(self):
        # Получение списка проектов
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()['content']

    def create_project(self, title, users):
        # Создание проекта
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "title": title,
            "users": users
        }

        resp = requests.post(self.url + 'projects', json=project,
                             headers=headers)
        return resp

    def get_project_by_id(self, project_id):
        # Получить проект по ID
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers)
        return resp

    def edit_project(self, project_id, new_deleted, new_title, new_users):
        # Изменение/удаление проекта
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "deleted": new_deleted,
            "title": new_title,
            "users": new_users
        }

        resp = requests.put(self.url + f'projects/{project_id}',
                            json=payload, headers=headers)
        return resp
