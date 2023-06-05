import pytest
import mongomock

from mongoengine import connect, disconnect


@pytest.fixture(scope="session", autouse=True)
def scope_session():
    connect(
        "mongoenginetest",
        host="mongodb://localhost",
        mongo_client_class=mongomock.MongoClient,
        alias="dummydb",
        uuidRepresentation="standard",
    )
    yield
    disconnect(alias="dummydb")
