from app import crud, models

pj_name = "my_project"
service_name = "my_service"


class TestService:
    def test_create_return_value(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)
        assert service.uuid
        assert service.name == service_name

    def test_create_data_result(self):
        project = crud.project.create(name=pj_name)
        created_service = crud.service.create(project=project, name=service_name)
        service = crud.service.get(project=project, uuid=created_service.uuid)
        assert created_service == service

    def test_delete_data_result(self):
        project = crud.project.create(name=pj_name)
        created_service = crud.service.create(project=project, name=service_name)
        deleted_service = crud.service.delete(
            project=project, uuid=created_service.uuid
        )
        service = crud.service.get(project=project, uuid=created_service.uuid)
        assert service is None
        assert created_service == deleted_service

    def test_return_instance(self):
        created_project = crud.project.create(name=pj_name)
        project = crud.project.get(uuid=created_project.uuid)

        create_ = crud.service.create(project=project, name=service_name)
        assert isinstance(create_, models.Service)

        get_ = crud.service.get(project=project, uuid=create_.uuid)
        assert isinstance(get_, models.Service)

        list_ = crud.service.get_list(project=project)
        assert isinstance(list_[0], models.Service)

        delete_ = crud.service.delete(project=project, uuid=create_.uuid)
        assert isinstance(delete_, models.Service)
