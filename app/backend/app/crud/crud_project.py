from app.crud.base import CRUDBase
from app import models, schemas


class Project(CRUDBase[models.Project, schemas.CreateProject]):
    ...


project = Project(models.Project)
