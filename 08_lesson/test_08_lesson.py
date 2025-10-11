from api_YouGile import YouGile
from credentials import (url, login, password, companyId, new_project,
                         empty_title, testing_title, edit_title,
                         edited_title, deleted_status, user, wrong_user)

api = YouGile(url, login, password, companyId)


def test_create_project_positive():
    # Получаем список проектов (записываем в список - количество)
    projects_before = api.get_projects()
    len_before = len(projects_before)
    # Создаем проект
    result = api.create_project(new_project, user)
    assert result.status_code == 201
    # Извлекаем ID созданного проекта
    response_data = result.json()
    new_id = response_data['id']
    # Получаем новый (после создания) список проектов
    projects_after = api.get_projects()
    len_after = len(projects_after)
    # Сравниваем списки, новый список должен быть +1
    assert len_after - len_before == 1
    # Проверяем что последний проект в списке имеет правильное название
    assert projects_after[-1]['title'] == new_project
    # Проверяем что последний проект в списке имеет правильный ID
    assert projects_after[-1]['id'] == new_id
    assert result.status_code == 201
    # Удаляем проект
    deleted_projects = api.edit_project(new_id, True, new_project, user)
    assert deleted_projects.status_code == 200


def test_create_project_negative():
    # Получаем список проектов (записываем в список - количество)
    projects_before = api.get_projects()
    len_before = len(projects_before)
    # Создаем проект с пустым названием
    result = api.create_project(empty_title, user)
    # Проверяем что выходит ошибка
    assert result.status_code == 400
    projects_after = api.get_projects()
    len_after = len(projects_after)
    # Сравниваем списки, новый список должен быть 0
    assert len_after - len_before == 0


def test_get_project_by_id_positive():
    #  Создаем проект
    result = api.create_project(testing_title, user)
    assert result.status_code == 201
    # Достаем айди
    project_id = result.json()['id']
    # Получаем проект по АЙДИ
    tested_project = api.get_project_by_id(
        project_id)
    assert tested_project.status_code == 200
    # Проверяем данные полученного проекта
    assert tested_project.json()['title'] == testing_title
    assert tested_project.json()['users'] == user

    deleted_projects = api.edit_project(project_id, True, testing_title, user)
    assert deleted_projects.status_code == 200


def test_get_project_by_id_negative():
    tested_project = api.get_project_by_id("1234346gfdd2323")
    assert tested_project.status_code == 404


def test_edit_project_positive():
    # Создаем проект и вытаскиваем id
    result = api.create_project(edit_title, user)
    assert result.status_code == 201
    project_id = result.json()['id']
    # Меняем название проекта
    res_edit = api.edit_project(project_id, deleted_status, edited_title, user)
    assert res_edit.status_code == 200
    # Проверяем название
    new_title = api.get_project_by_id(project_id)
    assert new_title.status_code == 200
    assert new_title.json()['title'] == edited_title

    deleted_projects = api.edit_project(project_id, True, edited_title, user)
    assert deleted_projects.status_code == 200


def test_edit_project_negative():
    # Создаем проект и вытаскиваем id
    result = api.create_project(testing_title, user)
    assert result.status_code == 201
    project_id = result.json()['id']
    # Меняем user проекта (неправильные данные)
    res_edit = api.edit_project(project_id, deleted_status,
                                testing_title, wrong_user)
    assert res_edit.status_code == 400

    deleted_projects = api.edit_project(project_id, True, testing_title, user)
    assert deleted_projects.status_code == 200
