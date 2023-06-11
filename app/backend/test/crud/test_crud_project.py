from app import crud, models

pj_name = "my_project"


class TestProject:
    def test_create_return_value(self):
        project = crud.project.create(name=pj_name)
        assert project.uuid
        assert project.name == pj_name

    def test_create_data_result(self):
        created_project = crud.project.create(name=pj_name)
        project = crud.project.get(uuid=created_project.uuid)
        assert created_project == project

    def test_delete_data_result(self):
        created_project = crud.project.create(name=pj_name)
        deleted_project = crud.project.delete(uuid=created_project.uuid)
        project = crud.project.get(uuid=created_project.uuid)
        assert project is None
        assert created_project == deleted_project

    def test_return_instance(self):
        create_ = crud.project.create(name=pj_name)
        get_ = crud.project.get(create_.uuid)
        list_ = crud.project.get_list()
        delete_ = crud.project.delete(create_.uuid)
        assert isinstance(create_, models.Project)
        assert isinstance(get_, models.Project)
        assert isinstance(list_[0], models.Project)
        assert isinstance(delete_, models.Project)
