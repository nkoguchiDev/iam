from mongoengine import Document
from mongoengine.fields import ReferenceField, BooleanField, StringField

from app.models import Service


class Backend(Document):
    uuid = StringField(unique=True, required=True)
    name = StringField(required=True)
    service = ReferenceField(Service)
    isPrivate = BooleanField(required=True)
    meta = {
        "db_alias": "dummydb",
        "collection": "backend",
    }
