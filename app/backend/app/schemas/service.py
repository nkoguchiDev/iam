from typing import Optional
from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    name: Optional[str] = None


class CreateService(ProjectBase):
    name: str
