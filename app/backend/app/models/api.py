from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField


class Service(Document):
    uuid = StringField(unique=True, required=True)
    name = StringField(required=True)
    meta = {
        "db_alias": "dummydb",
        "collection": "service",
    }
