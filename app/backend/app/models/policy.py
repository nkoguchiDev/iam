from app.models import BaseDocument


class Project(BaseDocument):
    projectId: str
    meta = {
        "db_alias": "dummydb",
        "collection": "role",
    }
