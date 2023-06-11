from typing import List, Optional

from app import models
from app.utils.generator import create_uuid


class Backend:
    def get_list(self, service: models.Service) -> List[models.Backend]:
        return models.Backend.objects(service=service)

    def get(self, service: models.Service, uuid: str) -> Optional[models.Backend]:
        data = models.Backend.objects(service=service, uuid=uuid).first()
        if data:
            return data

    def create(
        self, service: models.Service, name: str, isPrivate: bool = True
    ) -> models.Backend:
        uuid_ = create_uuid()
        return models.Backend(
            service=service, uuid=uuid_, name=name, isPrivate=isPrivate
        ).save()

    def delete(self, service: models.Service, uuid: str) -> Optional[models.Backend]:
        data = models.Backend.objects(service=service, uuid=uuid).first()
        data.delete()
        if data:
            return data


backend = Backend()
