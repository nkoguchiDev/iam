from app.models import BaseDocument


class Project(BaseDocument):
    meta = {
        "db_alias": "dummydb",
        "collection": "project",
    }
