from app import crud, models

pj_name = "my_project"
service_name = "my_service"
backend_name = "my_backend"


class TestService:
    def test_create_return_value(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)
        backend = crud.backend.create(service=service, name=backend_name)
        assert backend.uuid
        assert backend.name == backend_name

    def test_create_data_result(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)
        created_backend = crud.backend.create(service=service, name=backend_name)
        backend = crud.backend.get(service=service, uuid=created_backend.uuid)
        assert created_backend == backend

    def test_delete_data_result(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)
        created_backend = crud.backend.create(service=service, name=backend_name)
        deleted_backend = crud.backend.delete(
            service=service, uuid=created_backend.uuid
        )
        backend = crud.backend.get(service=service, uuid=created_backend.uuid)
        assert backend is None
        assert created_backend == deleted_backend

    def test_return_instance(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)

        create_ = crud.backend.create(service=service, name=backend_name)
        assert isinstance(create_, models.Backend)

        get_ = crud.backend.get(service=service, uuid=create_.uuid)
        assert isinstance(get_, models.Backend)

        list_ = crud.backend.get_list(service=service)
        assert isinstance(list_[0], models.Backend)

        delete_ = crud.backend.delete(service=service, uuid=create_.uuid)
        assert isinstance(delete_, models.Backend)
