from enum import Enum

from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField, EnumField

from app.models import Service, Backend


class ApiPlan(Enum):
    SIMPLE = "simple"
    CUSTOM = "custom"


class Api(Document):
    uuid = StringField(unique=True, required=True)
    name = StringField(required=True)
    plan = EnumField(ApiPlan, required=True)
    service = ReferenceField(Service)
    basePath = StringField(required=True)
    backend = ReferenceField(Backend)
    meta = {
        "db_alias": "dummydb",
        "collection": "api",
    }
