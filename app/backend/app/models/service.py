from mongoengine.fields import ReferenceField

from app.models import BaseDocument, Project


class Service(BaseDocument):
    project = ReferenceField(Project)
    meta = {
        "db_alias": "dummydb",
        "collection": "service",
    }
