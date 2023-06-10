from typing import List

from app import crud, models, schemas

pj_name = "my_project"
service_name = "my_service"
create_schema = schemas.CreateService(name=service_name)


class TestService:
    def test_create_return_value(self):
        project = crud.project.create(create_schema)
        service = crud.service.create(project, create_schema)
        assert isinstance(service, models.Service)
        assert service.uuid
        assert service.name == service_name

    def test_create_data_result(self):
        project = crud.project.create(create_schema)
        created_service = crud.service.create(project, create_schema)
        service = crud.service.get(project, uuid=created_service.uuid)
        assert created_service == service

    def test_delete_data_result(self):
        project = crud.project.create(create_schema)
        created_service = crud.service.create(project, create_schema)
        deleted_service = crud.service.delete(project, uuid=created_service.uuid)
        service = crud.service.get(project, uuid=created_service.uuid)
        assert service is None
        assert created_service == deleted_service
