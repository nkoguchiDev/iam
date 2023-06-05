from mongoengine import Document
from mongoengine.fields import StringField


class Project(Document):
    uuid = StringField(unique=True, required=True)
    name = StringField(required=True)

    meta = {
        "db_alias": "dummydb",
        "collection": "project",
    }
