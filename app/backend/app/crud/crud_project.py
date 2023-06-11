from typing import List, Optional

from app import models
from app.utils.generator import create_uuid


class Project:
    def get_list(self) -> List[models.Project]:
        return models.Project.objects()

    def get(self, uuid: str) -> Optional[models.Project]:
        data = models.Project.objects(uuid=uuid).first()
        if data:
            return data

    def create(self, name: str) -> models.Project:
        uuid_ = create_uuid()
        return models.Project(uuid=uuid_, name=name).save()

    def delete(self, uuid: str) -> Optional[models.Project]:
        data = models.Project.objects(uuid=uuid).first()
        data.delete()
        if data:
            return data


project = Project()
