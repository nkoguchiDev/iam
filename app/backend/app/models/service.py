from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField

from app.models import Project


class Service(Document):
    uuid = StringField(unique=True, required=True)
    name = StringField(required=True)
    project = ReferenceField(Project)
    meta = {
        "db_alias": "dummydb",
        "collection": "service",
    }
