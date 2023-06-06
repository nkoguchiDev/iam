from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel
from app.models import BaseDocument


ModelType = TypeVar("ModelType", bound=BaseDocument)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    def get(self, uuid: str) -> Optional[ModelType]:
        data = self.model.objects(uuid=uuid).first()
        if data:
            return data

    def get_list(self) -> List[ModelType]:
        return self.model.objects()

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        return self.model(**obj_in.dict()).save()

    def delete(self, uuid: str) -> Optional[ModelType]:
        data = self.model.objects(uuid=uuid).first()
        data.delete()
        if data:
            return data
