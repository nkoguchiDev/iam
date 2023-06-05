from typing import List

from app import crud, data


class TestProject:
    def test_create_return_value(self):
        pj_name = "my_project"
        project = crud.project.create(name=pj_name)
        assert isinstance(project, data.Project)
        assert project.uuid
        assert project.name == pj_name

    def test_create_data_result(self):
        pj_name = "my_project"
        created_project = crud.project.create(name=pj_name)
        projects = crud.project.get()
        assert isinstance(projects, List)
        assert isinstance(projects[0], data.Project)
        assert created_project in projects
