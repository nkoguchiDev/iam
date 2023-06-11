from app import crud

pj_name = "my_project"
service_name = "my_service"
backend_name = "my_backend"
api_name = "my_api"
api_plan = "simple"
api_basePath = "/v1/base"


class TestService:
    def test_create_return_value(self):
        project = crud.project.create(name=pj_name)
        service = crud.service.create(project=project, name=service_name)
        backend = crud.backend.create(service=service, name=backend_name)
        api = crud.api.create(
            name=api_name,
            plan=api_plan,
            service=service,
            basePath=api_basePath,
            backend=backend,
        )
        assert api.uuid
        assert api.name == api_name
