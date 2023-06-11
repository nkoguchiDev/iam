from typing import List, Optional

from app import models
from app.utils.generator import create_uuid


class Api:
    def get_list(self, service: models.Service) -> List[models.Api]:
        return models.Backend.objects(service=service)

    def get(self, service: models.Service, uuid: str) -> Optional[models.Api]:
        data = models.Backend.objects(service=service, uuid=uuid).first()
        if data:
            return data

    def create(
        self,
        name: str,
        plan: str,
        service: models.Service,
        basePath: str,
        backend: models.Backend,
    ) -> models.Api:
        uuid_ = create_uuid()
        return models.Api(
            uuid=uuid_,
            name=name,
            plan=plan,
            service=service,
            basePath=basePath,
            backend=backend,
        ).save()

    def delete(self, service: models.Service, uuid: str) -> Optional[models.Api]:
        data = models.Backend.objects(service=service, uuid=uuid).first()
        data.delete()
        if data:
            return data


api = Api()
