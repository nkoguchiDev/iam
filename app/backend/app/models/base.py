from mongoengine import Document
from mongoengine.fields import StringField


def create_uuid():
    from uuid import uuid4

    return str(uuid4())


class BaseDocument(Document):
    uuid = StringField(default=create_uuid, unique=True, required=True)
    name = StringField(required=True)

    meta = {"allow_inheritance": True}
