from typing import List

from app import crud, models, schemas

pj_name = "my_project"
create_schema = schemas.CreateProject(name=pj_name)


class TestProject:
    def test_create_return_value(self):
        project = crud.project.create(create_schema)
        assert isinstance(project, models.Project)
        assert project.uuid
        assert project.name == pj_name

    def test_create_data_result(self):
        created_project = crud.project.create(create_schema)
        project = crud.project.get(uuid=created_project.uuid)
        assert created_project in project

    def test_delete_data_result(self):
        created_project = crud.project.create(create_schema)
        deleted_project = crud.project.delete(uuid=created_project.uuid)
        project = crud.project.get(uuid=created_project.uuid)
        assert project is None
        assert created_project == deleted_project
