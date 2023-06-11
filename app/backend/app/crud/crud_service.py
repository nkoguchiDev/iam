from typing import List, Optional

from app import models
from app.utils.generator import create_uuid


class Service:
    def get_list(self, project: models.Project) -> List[models.Service]:
        return models.Service.objects(project=project)

    def get(self, project: models.Project, uuid: str) -> Optional[models.Service]:
        data = models.Service.objects(project=project, uuid=uuid).first()
        if data:
            return data

    def create(self, project: models.Project, name: str) -> models.Service:
        uuid_ = create_uuid()
        return models.Service(project=project, uuid=uuid_, name=name).save()

    def delete(self, project: models.Project, uuid: str) -> Optional[models.Service]:
        data = models.Service.objects(project=project, uuid=uuid).first()
        data.delete()
        if data:
            return data


service = Service()
