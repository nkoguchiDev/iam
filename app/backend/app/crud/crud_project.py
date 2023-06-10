from typing import List, Optional

from app import models, schemas


class Project:
    def get_list(self) -> List[models.Project]:
        return models.Project.objects()

    def get(self, uuid: str) -> Optional[models.Project]:
        data = models.Project.objects(uuid=uuid).first()
        if data:
            return data

    def create(self, obj_in: schemas.CreateProject) -> models.Project:
        return models.Project(**obj_in.dict()).save()

    def delete(self, uuid: str) -> Optional[models.Project]:
        data = models.Project.objects(uuid=uuid).first()
        data.delete()
        if data:
            return data


project = Project()
