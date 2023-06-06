from typing import List, Optional

from app import data, model


def create_uuid():
    from uuid import uuid4

    return str(uuid4())


class Project:
    def get(self) -> List[data.Project]:
        projects = model.Project.objects()
        return [
            data.Project(uuid=project.uuid, name=project.name) for project in projects
        ]

    def get_by_uuid(self, uuid: str) -> Optional[data.Project]:
        project = model.Project.objects(uuid=uuid).first()
        if project:
            return data.Project(uuid=project.uuid, name=project.name)

    def create(self, name: str) -> data.Project:
        uuid = create_uuid()
        project = model.Project(uuid=uuid, name=name)
        project.save()
        return data.Project(uuid=project.uuid, name=project.name)

    def delete(self, uuid: str) -> Optional[data.Project]:
        project = model.Project.objects(uuid=uuid).first()
        project.delete()
        if project:
            return data.Project(uuid=project.uuid, name=project.name)


project = Project()
