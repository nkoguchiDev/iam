from typing import Optional
from pydantic import BaseModel, UUID4


# Shared properties
class ProjectBase(BaseModel):
    uuid: Optional[str] = None
    name: Optional[str] = None


class CreateProject(ProjectBase):
    name: str
